from django.core.management.base import BaseCommand
from django.http import HttpResponse

import pandas as pd
from pandas import Series, DataFrame

from datetime import datetime,timedelta
from datetime import date as dt_date

from race.models import Race

import requests

class Command(BaseCommand):

    #文章考えるのダルいからとりあえずこれ
    help="scraping"

    def handle(self,*args,**options):
        try:
            url="https://race.netkeiba.com/top/schedule.html"
            table=pd.read_html(url)[0]
            race_number=table.shape[0] #重賞レースの数
            print("スクレイピングに成功しました")
        except Exception as e:
            print(f"エラーが発生しました: {e}")

        for i in range(race_number):

            #Raceクラスのインスタンスを作成
            race=Race(name=table.iloc[i,1],place=table.iloc[i,3],date=table.iloc[i,0],grade=table.iloc[i,2],d_check=1,number=i)
            race.save()

