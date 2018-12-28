#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 08:07:32 2018

@author: mutecypher
"""

import matplotlib.pyplot as plt

plt.close('all')
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000,4), index=ts.index, columns = list('ABCD'))
plt.figure();
df.plot();
df = df.cumsum()
df.plot()

fileName = "https://library.startlearninglabs.uw.edu/DATASCI410/Datasets/JitteredHeadCount.csv"
import pandas as pd
import numpy as np


jitter_head = pd.read_csv(fileName)
print(jitter_head.head())
jitter_head.describe()
import seaborn as sbn
%matplotlib inline
import matplotlib.pyplot as plt
ax = plt.figure(figsize=(12, 12)).gca() # define axis
jitter_head.plot.scatter(x = 'Hour', y = 'HeadCount', ax = ax)
ax.set_title('Head Count versus Hour') # Give the plot a main title
ax.set_ylabel('Head Count')# Set text for y axis
ax.set_xlabel('Hour')


ax = plt.figure(figsize=(12, 12)).gca() # define axis
jitter_head.plot.hexbin(x = 'DayOfWeek', y = 'HeadCount', gridsize = 25, ax = ax)
ax.set_title('Head Count versus Day Of Week') # Give the plot a main title
ax.set_ylabel('Head Count')# Set text for y axis
ax.set_xlabel('Day Of Week')

##ax = plt.figure(figsize=(12, 12)).gca()
sbn.catplot(x = "Hour", y = "HeadCount", data = jitter_head, col = "GameCode", col_wrap = 5, kind = "box")


test = jitter_head.loc[jitter_head['GameCode']== 'BA']

test.head()
seven = jitter_head.loc[(jitter_head['GameCode']== 'S6') & (jitter_head['Hour'] == 7)].sum()
eight = jitter_head.loc[(jitter_head['GameCode']== 'S6') & (jitter_head['Hour'] == 8)].sum()
nine = jitter_head.loc[(jitter_head['GameCode']== 'S6') & (jitter_head['Hour'] == 9)].sum()
df_list = [seven, eight, nine]

tryit = seven.merge( eight, on = 'Hour', how = 'right')
print(seven)
sbn.catplot(x = "Hour", y = "TablesClosed", data = jitter_head, col = "GameCode", col_wrap = 5, kind = "box")
trap = pd.crosstab([jitter_head.Hour, jitter_head.HeadCount],jitter_head.GameCode, margins=False)
num_games = trap.apply(sum, axis = 0)
trap = trap.div(num_games,axis = 1)
trip = pd.melt(jitter_head, ['GameCode'])
num_games.head()
print(num_games)
print(trap)

game_list = ['BA', 'CR', 'RR']
timez = [7, 8, 9]
summy = jitter_head.loc[(jitter_head['GameCode'].isin(['BA', 'CR', 'RR'])) & (jitter_head['Hour'].isin([7,8,9]))].sum()
print(summy)
print(seven.loc['HeadCount'])
blech = [1]
guesses = pd.DataFrame({'HeadCount': seven.loc['HeadCount'], 'TablesOcc' : seven.loc['TablesOcc'], 'TableOpen' : seven.loc['TablesOpen'], 'Hours' : 7}, index = blech)
