from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),
    re_path(r'^(\d+)/(\d+)/$', views.detail),
    re_path(r'^grades/$', views.grades),
    path('students/', views.students),
    re_path(r'^grades/(\d+)/$', views.gredeStudent),
    path('addstudent/', views.addstudent),
    path('addstudent2/', views.addstudent2),
    path('student3/', views.student3),
    re_path(r'^student4/(\d+)/$', views.student4),
    path('search/', views.search),
    path('FQ/', views.FQ),

]


