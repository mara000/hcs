from django.shortcuts import render
from random import randrange
# Create your views here.

def homepage(request):
    return render(request, "homepage.html")


def randomExperiment(request):
    pages = ['emoji.html', 'alphanumeric.html', 'emojiandalpha.html']
    random_page = pages[randrange(3)]

    return render(request, random_page)

