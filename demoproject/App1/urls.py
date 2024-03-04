from django.urls import path 
from .views import home_view, exhaust, ridinggears, helmet
from App1.views import home_view, exhaust, ridinggears, helmet


urlpatterns =[
    path ("",home_view, name="home"),
    path ("exhaust/",exhaust, name="exhaust"),
    path ("ridinggears/",ridinggears, name="ridinggears"),
    path ("helmet/",helmet, name="helmet"),
]

