from django.shortcuts import render
from random import randrange
from hcs_app.models import User
# Create your views here.

def homepage(request):
    return render(request, "homepage.html")


def randomExperiment(request):
    pages = ['emoji.html', 'alphanumeric.html', 'emojiandalpha.html']
    random_page = pages[randrange(3)]

    return render(request, random_page)

def showDisplay(request, display_name):
    if display_name == "emoji":
        return render(request, "emoji.html")
    if display_name == "emojiandalpha":
        return render(request, "emojiandalpha.html")
    if display_name == "alpha":
        return render(request, "alphanumeric.html")
    
    
    return render(request, "homepage.html")


def receiveData(request):
    if request.method == "POST":
        newuser = User(
            firstname=request.POST['name'],
            password=request.POST['pass'],
        )
        newuser.save()



