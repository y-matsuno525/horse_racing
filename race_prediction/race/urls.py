from django.urls import path
from . import views

urlpatterns=[

    #テンプレートで　<a href="{% url 'race' object.number %}">　とすると name="race" のページへ object.number を引数として移動する
    path('',views.home,name="home"),
    path('race/<int:id>/',views.race,name="race"),
    path('race/voted/',views.voted,name="voted"),
]
