from django.shortcuts import render
from django.http import HttpResponse

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

from .models import Race

#グローバル変数
table=pd.read_html("https://race.netkeiba.com/top/schedule.html")[0]
race_number=table.shape[0] #重賞レースの数
date_list=[]
name_list=[]
grade_list=[]
place_list=[]
object_list=[]
url_list=['']*race_number
for k in range(race_number):
    date_list.append(table.iloc[k,0])
    name_list.append(table.iloc[k,1])
    grade_list.append(table.iloc[k,2])
    place_list.append(table.iloc[k,3])

#ホーム画面
def home(request):

    dt_now = dt_date.today()
    m_now=dt_now.month
    d_now=dt_now.day

    #初回のみスクレイピングを行う
    if Race.objects.count() == 0:

        for i in range(race_number):
            
            #一週間以内に開催されるかどうかを判定
            m=int(date_list[i][0:2])
            d=int(date_list[i][3:5])
            one_week_later=dt_now+timedelta(days=6)
            race_date=dt_date(2024,m,d)
            if dt_now <= race_date <= one_week_later:
                d_check=0
            else:
                d_check=1

            #Raceクラスのインスタンスを作成
            race=Race(name_list[i],name_list[i],place_list[i],date_list[i],grade_list[i],d_check,i)
            object_list.append(race)

    params={
        'objects':object_list,
            }     

    return render(request,"race/home.html",params)
    

#レース情報を表示するページ
def race(request,number):

    #選択されたレースのURLを生成
    if place_list[number] == '阪神':
        url_list[number]="https://www.keibalab.jp/db/race/2024"+date_list[number][0:2]+date_list[number][3:5]+"0911/tokubetsu.html?kind=simple"
    elif place_list[number] == '中山':
        url_list[number]="https://www.keibalab.jp/db/race/2024"+date_list[number][0:2]+date_list[number][3:5]+"0611/tokubetsu.html?kind=simple"
    elif place_list[number]=='福島':
        url_list[number]="https://www.keibalab.jp/db/race/2024"+date_list[number][0:2]+date_list[number][3:5]+"0311/tokubetsu.html?kind=simple"
    
    #選択されたレースの情報をスクレイピング
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url=url_list[number], headers=headers)
    response.encoding = response.apparent_encoding
    df = pd.read_html(response.text)[0]

    #必要なレース情報を抽出(枠番が確定したあとにも正しく抽出できるか確認する)
    horse_list=[] #馬の名前を格納するリスト
    for j in range(df.shape[0]):
        horse_list.append(df.iloc[j,0])
    title=table.iloc[number,0]

    params={
        "horses":horse_list,
        "title":title
    }

    return(request,"race/race.html",params)