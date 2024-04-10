import pandas as pd
import numpy.random as random
import scipy as sp
import numpy as np
from pandas import Series, DataFrame

from datetime import datetime,timedelta
from datetime import date as dt_date

import requests

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

table=pd.read_html("https://race.netkeiba.com/top/schedule.html")[0]

race_number=table.shape[0]
date_list=[]
name_list=[]
grade_list=[]
place_list=[]
for i in range(race_number):
    date_list.append(table.iloc[i,0])
    name_list.append(table.iloc[i,1])
    grade_list.append(table.iloc[i,2])
    place_list.append(table.iloc[i,3])

dt_now = dt_date.today()
m_now=dt_now.month
d_now=dt_now.day

place_code=['']*race_number
url_list=['']*race_number

for i in range(race_number):
    m=int(date_list[i][0:2])
    d=int(date_list[i][3:5])
    one_week_later=dt_now+timedelta(days=6)
    race_date=dt_date(2024,m,d)
    if dt_now <= race_date <= one_week_later:
        if place_list[i] == '阪神':
            url_list[i]="https://www.keibalab.jp/db/race/2024"+date_list[i][0:2]+date_list[i][3:5]+"0911/tokubetsu.html?kind=simple"
        elif place_list[i] == '中山':
            url_list[i]="https://www.keibalab.jp/db/race/2024"+date_list[i][0:2]+date_list[i][3:5]+"0611/tokubetsu.html?kind=simple"
        elif place_list[i]=='福島':
            url_list[i]="https://www.keibalab.jp/db/race/2024"+date_list[i][0:2]+date_list[i][3:5]+"0311/tokubetsu.html?kind=simple"
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url=url_list[i], headers=headers)
        response.encoding = response.apparent_encoding
        df = pd.read_html(response.text)[0]
        exec("horse_list_"+str(i)+"=[]")
        for j in range(df.shape[0]):
            exec("horse_list_"+str(i)+".append(df.iloc[j,0])")
        exec("test_list_1=horse_list_"+str(i))
        exec("race_information_list_"+str(i)+"=[]")
        exec("race_information_list_"+str(i)+".extend([table.iloc[i,0],table.iloc[i,1],table.iloc[i,2],table.iloc[i,3]])")
        exec("test_list_2=race_information_list_"+str(i))

