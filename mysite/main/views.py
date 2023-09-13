from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("hello")

def v1(response):
    return HttpResponse("Hello world")