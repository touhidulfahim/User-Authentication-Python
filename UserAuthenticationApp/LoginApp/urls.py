from django.conf.urls import url
from django.urls import path
from LoginApp import views

app_name="LoginApp"



urlpatterns=[
    path('', views.index, name='index')
]
