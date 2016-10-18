from django.shortcuts import render
import datetime


def welcome(request):
    context = {}
    return render(request, 'myschool/students.html', context)


def daytime(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'myschool/time.html', context)


def students(request):
    context = {}
    return render(request, 'myschool/students.html', context)


def classes(request):
    context = {}
    return render(request, 'myschool/classes.html', context)


def payments(request):
    context = {}
    return render(request, 'myschool/payments.html', context)
