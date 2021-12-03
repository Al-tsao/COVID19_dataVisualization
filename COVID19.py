#載入模組
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly as py

import folium

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import math
import random
from datetime import timedelta

import warnings
warnings.filterwarnings('ignore')

#設定
cnf = '#393e46'
dth = '#ff2e63'
rec = '#21bf73'
act = '#fe9801'
# py.offline.init_notebook_mode(connected = True) #要讓plotly離線使用

#載入資料
df = pd.read_csv('covid_19_data_cleaned.csv', parse_dates = ['Date'])
df['Province/State'] = df['Province/State'].fillna("") #把欄位中的NaN用空格取代
country_daywise = pd.read_csv('country_daywise.csv', parse_dates = ['Date'])
countrywise = pd.read_csv('countrywise.csv')
daywise = pd.read_csv('daywise.csv', parse_dates = ['Date'])

#整理資料
confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()
deaths = df.groupby('Date').sum()['Deaths'].reset_index()

#檢視資料
# print(df.isnull().sum()) #查看是否有空值
# print(df.info())

#篩選資料
df.query('Country == "US"').groupby('Date').sum()['Confirmed'].reset_index()
mask = df['Country'] == 'US'
df[mask].groupby('Date').sum()['Confirmed'].reset_index()


#繪圖
fig = go.Figure()
fig.add_trace(go.Scatter(x = confirmed['Date'], y = confirmed['Confirmed']))
fig.show()
