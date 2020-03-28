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

import pandas as pd
import numpy as np
from pathlib import Path
# %autosave 0

repo = Path.home() / "data-stuff/COVID-19"
data_dir = repo / "csse_covid_19_data/csse_covid_19_time_series"
confirmed = pd.read_csv(data_dir / "time_series_19-covid-Confirmed.csv")
deaths = pd.read_csv(data_dir / "time_series_19-covid-Deaths.csv")

cols_to_drop = ["Lat", "Long"]
name_map = {"Country/Region": "country",
           "Province/State": "state"}
confirmed = confirmed.drop(columns=cols_to_drop).rename(columns=name_map)
deaths = deaths.drop(columns=cols_to_drop).rename(columns=name_map)

confirmed = (confirmed[confirmed["country"] == "US"]
             .drop(columns=["country"])
             .set_index("state")
             .transpose())
deaths = (deaths[deaths["country"] == "US"]
          .drop(columns=["country"])
          .set_index("state")
          .transpose())

confirmed.index = pd.to_datetime(confirmed.index)
deaths.index = pd.to_datetime(deaths.index)

states = ["New York", "Washington", "California", "New Jersey", "Florida", "Illinois", "Michigan", "Louisiana"]
options = {"logy": False, "figsize": (13,8)}

confirmed[states].last("10D").plot(title="Confirmed US Cases, by State", **options)

deaths[states].last("10D").plot(title="US Deaths, by State", **options)

confirmed[states].last("14D")
