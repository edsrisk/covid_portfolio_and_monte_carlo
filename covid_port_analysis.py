import pandas as pd
from pathlib import Path
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# Covid Data United States
cdc_covid_preview = pd.read_csv('case_daily_trends__united_states.csv', sep=';')
cdc_covid_preview.head()
us_covid_df = pd.read_csv('case_daily_trends__united_states.csv', index_col='Date', infer_datetime_format=True, parse_dates=True, skiprows=3)
print(us_covid_df.head())
print(us_covid_df.tail())

# Dow Jones Industrial Average Data
dowjones_df = pd.read_csv(Path('DowJones.csv'), index_col='Date', infer_datetime_format=True, parse_dates=True)
print(dowjones_df.head())
print(dowjones_df.tail())

