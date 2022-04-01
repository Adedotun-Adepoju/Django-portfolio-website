from django.urls import path, include
from rest_framework import routers
from loanprediction import views 

app_name = "loanprediction" 

router = routers.DefaultRouter()
router.register('loanprediction', views.ApplicantsView)
urlpatterns = [
    path("", views.index, name='index'),
    path("api/", include(router.urls)),
    path("predict/", views.form, name='forms'),
]