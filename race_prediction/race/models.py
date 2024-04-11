from django.db import models

class Race(models.Model):
    race_name=models.CharField(max_length=20)
    race_place=models.CharField(max_length=10)
    race_type_and_distance=models.IntegerField()
    race_day_of_the_week=models.CharField(max_length=10)
    race_grade=models.CharField(max_length=10)

class Horse(models.Model):
    horse_race=models.ForeignKey(Race,on_delete=models.CASCADE)
    horse_name=models.CharField(max_length=20)
    horse_age=models.IntegerField()
    horse_gender=models.CharField(max_length=10)
    horse_number=models.IntegerField()
    horse_horseman=models.CharField(max_length=20)



