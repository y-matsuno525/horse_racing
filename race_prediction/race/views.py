from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

import random

from datetime import datetime,timedelta
from datetime import date as dt_date

import requests

from .models import Race,Horse
from .forms import vote

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
def race_info(request,id):
    
    race=Race.objects.get(number=id)
    url=""

    #選択されたレースのURLを生成
    if race.place=='阪神':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0911/tokubetsu.html?kind=simple"
    elif race.place=='中山':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0611/tokubetsu.html?kind=simple"
    elif race.place=='福島':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0311/tokubetsu.html?kind=simple"
    elif race.place=='東京':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0511/tokubetsu.html?kind=simple"
    elif race.place=='京都':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0411/tokubetsu.html?kind=simple"
    elif race.place=='新潟':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0311/tokubetsu.html?kind=simple"
    elif race.place=='小倉':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"1011/tokubetsu.html?kind=simple"
    elif race.place=='中京':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0711/tokubetsu.html?kind=simple"
    elif race.place=='函館':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0211/tokubetsu.html?kind=simple"
    elif race.place=='札幌':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0111/tokubetsu.html?kind=simple"
    
    #選択されたレースの情報をスクレイピング
    try:
        #ユーザーエージェントを複数用意する
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
            # 他にも追加可能
        ]
        headers = {'User-agent': random.choice(user_agents)}
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        df = pd.read_html(response.text)[0]

    #エラー処理はchatgptによるもの。見直す必要あるかも。
    except requests.RequestException as e:
        return HttpResponse(f"Error fetching page: {e}", status=500)
    except ValueError:
        return HttpResponse("Error parsing the HTML table.", status=500)

    #必要なレース情報を抽出(枠番が確定したあとにも正しく抽出できるか確認する)
    horses=[]
    for j in range(df.shape[0]):
        if not Horse.objects.get(name=df.iloc[j,0]).exists():
            horse=Horse(race_name=race.name,name=df.iloc[j,0])
            horse.save()
            horses.append(horse.name)

    

    params={
        "title":race.name,
        "id":id,
        "horses":horses,
        "form":vote(horses),
    }

    return render(request,"race/race.html",params)

def voted(request):
    if (request.method=="POST"):
        horse=Horse.objects.filter(name=request.POST['choice'])
        horse.vote_count += 1
        horse.save()
        
        

