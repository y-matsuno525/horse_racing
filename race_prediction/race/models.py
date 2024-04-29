from typing import Any
from django.db import models

#後でマイグレーションするのを忘れずに！
class Race(models.Model):
    name=models.CharField(max_length=20) 
    place=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    grade=models.CharField(max_length=10)
    d_check=models.IntegerField(default=1) #一週間以内に開催されるなら0、それ以外は1
    number=models.IntegerField(default=1)

class Horse(models.Model):
    race_name=models.ForeignKey(Race,on_delete=models.CASCADE,related_name="horses")
    name=models.CharField(max_length=100)
    vote_count=models.IntegerField(default=0)

   

