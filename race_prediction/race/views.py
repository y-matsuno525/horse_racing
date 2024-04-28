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
#テスト済み

#ホーム画面
def home(request):

    dt_now = dt_date.today()
    m_now=dt_now.month
    d_now=dt_now.day

    objects=Race.objects.all()

    for object in objects:
            
        #一週間以内に開催されるかどうかを判定
        m=int(object.date[0:2])
        d=int(object.date[3:5])
        one_week_later=dt_now+timedelta(days=6)
        race_date=dt_date(2024,m,d)
        if dt_now <= race_date <= one_week_later:
            object.d_check=0
            object.save()
        else:
            object.d_check=1
            object.save()

    params={
        'objects':objects,
            }     

    return render(request,"race/home.html",params)
    

#レース情報を表示するページ
def race(request,id):

    #選択されたレースのURLを生成
    if place_list[id]=='阪神':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0911/tokubetsu.html?kind=simple"
    elif place_list[id]=='中山':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0611/tokubetsu.html?kind=simple"
    elif place_list[id]=='福島':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0311/tokubetsu.html?kind=simple"
    elif place_list[id]=='東京':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0511/tokubetsu.html?kind=simple"
    elif place_list[id]=='京都':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0411/tokubetsu.html?kind=simple"
    elif place_list[id]=='新潟':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0311/tokubetsu.html?kind=simple"
    elif place_list[id]=='小倉':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"1011/tokubetsu.html?kind=simple"
    elif place_list[id]=='中京':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0711/tokubetsu.html?kind=simple"
    elif place_list[id]=='函館':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0211/tokubetsu.html?kind=simple"
    elif place_list[id]=='札幌':
        url_list[id]="https://www.keibalab.jp/db/race/2024"+date_list[id][0:2]+date_list[id][3:5]+"0111/tokubetsu.html?kind=simple"
    
    #選択されたレースの情報をスクレイピング
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url=url_list[id], headers=headers)
    response.encoding = response.apparent_encoding
    df = pd.read_html(response.text)[0]

    #必要なレース情報を抽出(枠番が確定したあとにも正しく抽出できるか確認する)
    horse_list=[] #馬の名前を格納するリスト
    for j in range(df.shape[0]):
        horse_list.append(df.iloc[j,0])
    title=table.iloc[id,0]

    params={
        "horses":horse_list,
        "title":title,
        "id":id,
    }

    return render(request,"race/race.html",params)