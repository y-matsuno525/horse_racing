from django.urls import path
from . import views

urlpatterns=[

    #テンプレートで　<a href="{% url 'race' object.number %}">　とすると name="race" のページへ object.number を引数として移動する
    path('',views.home,name="home"),
    path('race_info/<int:id>/',views.race_info,name="race_info"),
    path('race_info/voted/',views.voted,name="voted"),
]
