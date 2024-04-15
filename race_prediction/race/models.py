from typing import Any
from django.db import models

#後でマイグレーションするのを忘れずに！
class Race(models.Model):
    name=models.CharField(max_length=20) 
    place=models.CharField(max_length=10)
    type=models.IntegerField()
    date=models.CharField(max_length=10)
    grade=models.CharField(max_length=10)
    check=models.IntegerField() #一週間以内に開催されるなら0、それ以外は1

    #引数をもとにインスタンスを生成
    def __init__(self,name,place,week,grade):
        self.name=name
        self.place=place
        self.week=week
        self.grade=grade
        

class Horse(models.Model):
    horse_race=models.ForeignKey(Race,on_delete=models.CASCADE)
    horse_name=models.CharField(max_length=20)
    horse_age=models.IntegerField()
    horse_gender=models.CharField(max_length=10)
    horse_number=models.IntegerField()
    horse_horseman=models.CharField(max_length=20)



