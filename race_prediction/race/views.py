from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

import random

from datetime import datetime,timedelta
from datetime import date as dt_date

import requests

from .models import Race,Horse
from .forms import VoteForm


from django.contrib.auth.decorators import login_required





#レース一覧画面
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
@login_required
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
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0811/tokubetsu.html?kind=simple"
    elif race.place=='新潟':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0411/tokubetsu.html?kind=simple"
    elif race.place=='小倉':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"1011/tokubetsu.html?kind=simple"
    elif race.place=='中京':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0711/tokubetsu.html?kind=simple"
    elif race.place=='函館':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0211/tokubetsu.html?kind=simple"
    elif race.place=='札幌':
        url="https://www.keibalab.jp/db/race/2024"+race.date[0:2]+race.date[3:5]+"0111/tokubetsu.html?kind=simple"
    

    #選択されたレースの情報をスクレイピング
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    df = pd.read_html(response.text)[0]
    


    for j in range(df.shape[0]):
        if not Horse.objects.filter(name=df.iloc[j,0]).exists():
            horse=Horse(race_name=race,name=df.iloc[j,0],vote_count=0)
            horse.save()
        else:
            horse=Horse.objects.get(name=df.iloc[j,0])
            horse.race_name=race
            horse.save()


    
    horses=Horse.objects.filter(race_name=race).order_by('vote_count').reverse()

    current_rank=0
    previous_vote_count=None

    for horse in horses:
        if horse.vote_count != previous_vote_count:
            current_rank += 1
            horse.rank = current_rank
            previous_vote_count=horse.vote_count
        else:
            horse.rank = current_rank

    form=VoteForm(horses=horses)

    params={
        "title":race.name,
        "id":id,
        "horses":horses,
        "form":form,
    }

    return render(request,"race/race_info.html",params)


@login_required
def voted(request):
    if (request.method=="POST"):
        horse=Horse.objects.get(name=request.POST['choice'])
        horse.vote_count += 1
        horse.save()
    
    return render(request,"race/voted.html")




