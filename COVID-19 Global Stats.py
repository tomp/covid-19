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

# ### COVID-19 Global Stats
# This notebook lets you examine and plot the data shared throught the JHU CSSE git repo
#
#     git clone https://github.com/CSSEGISandData/COVID-19.git
#
# The git repo provides country-by-country (and province by province, for some countries) daily stats for confirmed COVID-19 cases, and deaths.
#
# This notebook pulls just the country-level data out of the repo.  An accompanying notebook does the same for the US state-by-state stats.

import pandas as pd
import numpy as np
from pathlib import Path
# %autosave 0

# You will need to set 'repo' to the absolute pathname for the COVID-19 repo, on your system.
repo = Path.home() / "data-stuff/COVID-19"

data_dir = Path(repo) / "csse_covid_19_data/csse_covid_19_time_series"
confirmed = pd.read_csv(data_dir / "time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv(data_dir / "time_series_covid19_deaths_global.csv")

cols_to_drop = ["Province/State", "Lat", "Long"]
confirmed = confirmed.drop(columns=cols_to_drop).rename(columns={"Country/Region": "country"})
deaths = deaths.drop(columns=cols_to_drop).rename(columns={"Country/Region": "country"})

confirmed = confirmed.groupby("country").agg(np.sum).transpose()
deaths = deaths.groupby("country").agg(np.sum).transpose()

confirmed.index = pd.to_datetime(confirmed.index)
deaths.index = pd.to_datetime(deaths.index)

# +
# list(confirmed.columns)
# -

countries = ["China", "Italy", "Iran", "US", "Germany", "France", "Spain", "United Kingdom"]
options = {"logy": True, "figsize": (13,8)}

confirmed[countries].last("30D").plot(title="Confirmed Cases, by Country", **options)

deaths[countries].last("30D").plot(title="Deaths, by Country", **options)

confirmed[countries].last("10D")

deaths[countries].last("10D")


