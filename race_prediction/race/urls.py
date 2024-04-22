from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('race/<int:id>/',views.race,name="race"),
]
