from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response):
    return HttpResponse("hello")

def v1(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("%s" % ls.item_set.get())
def v2(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("%s" % ls.name)