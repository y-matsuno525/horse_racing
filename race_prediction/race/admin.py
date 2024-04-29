from django.contrib import admin
from .models import Race

from django.core.management.base import BaseCommand
from django.http import HttpResponse

import pandas as pd
from pandas import Series, DataFrame

from datetime import datetime,timedelta
from datetime import date as dt_date

from race.models import Race

from django.contrib.auth.models import Group

from .models import User



class Command(BaseCommand):

    #文章考えるのダルいからとりあえずこれ
    help="scraping"

    def handle(self,*args,**options):

        table=pd.read_html("https://race.netkeiba.com/top/schedule.html")[0]
        race_number=table.shape[0] #重賞レースの数

        for i in range(race_number):

            #Raceクラスのインスタンスを作成
            race=Race(name=table.iloc[i,1],place=table.iloc[i,3],date=table.iloc[i,0],grade=table.iloc[i,2],d_check=1,number=i)
            race.save()
