from django.contrib import admin
from django.urls import path, re_path
from qa import views

#urlpatterns = [re_path(r'/question/<int>', views.test, name='test') ]
urlpatterns = [path('', views.test, name='test')]
