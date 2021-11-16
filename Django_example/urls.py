from django.conf.urls import url
from django.urls import path
from Django_example import views

urlpatterns = [
    path('', views.index, name='index'),
    

]