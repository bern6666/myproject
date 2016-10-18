from django.shortcuts import render
from django.http import HttpResponse
import datetime


def welcome(request):
    welcometext = "<h1>Welcome at My Music School</h1>"
    return HttpResponse(welcometext)


def daytime(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'myschool/time.html', context)
