from typing import Any
from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings



#後でマイグレーションするのを忘れずに！
class Race(models.Model):
    name=models.CharField(max_length=20) 
    place=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    grade=models.CharField(max_length=10)
    d_check=models.IntegerField(default=1) #一週間以内に開催されるなら0、それ以外は1
    number=models.IntegerField(default=1)
    rank=models.IntegerField(default=0)

class Horse(models.Model):
    race_name=models.ForeignKey(Race,on_delete=models.CASCADE,related_name="horses")
    name=models.CharField(max_length=100)
    vote_count=models.IntegerField(default=0)

#ユーザーの投票履歴
class Race_history(models.Model):
    race=models.ForeignKey(Race,on_delete=models.CASCADE)#投票したレース
    user=models.OneToOneField(settings.AUTH_USER_MODEL)#投票したユーザー
    voted_horse=models.ForeignKey(Horse,on_delete=models.CASCADE)#投票先の馬名

