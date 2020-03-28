# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### COVID-19 US Stats
# This notebook lets you examine and plot the data shared through the JHU CSSE git repo
#
#     git clone https://github.com/CSSEGISandData/COVID-19.git
#
# The git repo provides country-by-country (and province by province, for some countries) daily stats for confirmed COVID-19 cases, and deaths.
#
# This notebook pulls just the state-level US data out of the repo.  An accompanying notebook does the same for the country-level stats.
#
# _NOTE_ After Mar 23, 2020, the state-level data is no longer in the global time-series spreadsheet.  So, here we pull it from the daily reports and stitch it back together into a timeline.

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import date
# %autosave 0

# You will need to set 'repo' to the absolute pathname for the COVID-19 repo, on your system.
repo = Path.home() / "data-stuff/COVID-19"

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
"District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
"Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
"Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
"New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
"Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
"Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",]

# +
name_map = {"Country/Region": "country",
           "Province/State": "state",
           "Country_Region": "country",
           "Province_State": "state",
           "Admin2": "county",
           "Confirmed": "confirmed",
           "Deaths": "deaths"}
    
def load_daily_report(pathname):
    df = pd.read_csv(pathname)
    df = df.rename(columns=name_map)
    m, d, y = [int(v) for v in str(Path(pathname).name).replace(".csv", "").split("-")]
    dt = date(y, m, d)
    if "state" not in df.columns:
        return dt, None

    df = df[df["country"] == "US"]
    if dt < date(2020, 3, 22) and "county" in df.columns:
        df = df[df["county"].isnull()]
    df = df[["state", "confirmed", "deaths"]]
    df = df.groupby("state").agg(np.sum)
    return dt, df


# +
data_dir = Path(repo) / "csse_covid_19_data/csse_covid_19_daily_reports"

dated_files = []
for file in data_dir.glob("*-*-2020.csv"):
    m, d, y = [int(v) for v in str(file.name).replace(".csv", "").split("-")]
    dated_files.append(((y, m, d), file))

confirmed = pd.DataFrame(index=states)
deaths = pd.DataFrame(index=states)

for _, file in sorted(dated_files):
    dt, df = load_daily_report(file)
    if df is not None:
        confirmed[dt] = df["confirmed"]
        deaths[dt] = df["deaths"]
        
confirmed = confirmed.transpose()
deaths = deaths.transpose()

confirmed.index = pd.to_datetime(confirmed.index)
deaths.index = pd.to_datetime(deaths.index)
# -

states = ["New York", "Washington", "California", "New Jersey", "Florida", "Illinois", "Michigan", "Louisiana"]
options = {"logy": False, "figsize": (13,8)}

confirmed[states].last("10D").plot(title="Confirmed US Cases, by State", **options)

deaths[states].last("10D").plot(title="US Deaths, by State", **options)

confirmed[states].last("10D")

deaths[states].last("10D")


