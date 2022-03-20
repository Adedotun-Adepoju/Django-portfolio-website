from django.urls import path

from loanprediction import views 

app_name = "loanprediction" 

urlpatterns = [
    path("", views.index, name='index'),
    path("predict/", views.form, name='forms'),
    path("result/", views.result, name='result')
]