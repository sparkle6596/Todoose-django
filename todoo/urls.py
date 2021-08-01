from django.urls import path
from .views import todo_add
from django.shortcuts import render

urlpatterns=[
    path("todoooadd",todo_add,name="adding"),
    path("",lambda request:render(request,"index.html"),name="index")

]