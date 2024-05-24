from django.urls import path
from .import views

urlpatterns =[
    path('', views.home, name='home'),
    path('insert_student', views.insert_student, name='insert_student'),
]