from typing import Any
from django.db import models

#後でマイグレーションするのを忘れずに！
class Race(models.Model):
    name=models.CharField(max_length=20) 
    place=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    grade=models.CharField(max_length=10)
    d_check=models.IntegerField() #一週間以内に開催されるなら0、それ以外は1


