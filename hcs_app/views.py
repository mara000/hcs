from django.shortcuts import render, redirect
from random import randrange
from hcs_app.models import Participant
from django.contrib import messages
from django.http import HttpResponseBadRequest

def homepage(request):
    storage = messages.get_messages(request)
    context_dict = {}
    context_dict["show_response"] = storage

    return render(request, "homepage.html", context=context_dict)


def randomExperiment(request):
    if request.method == "POST":
        if request.POST['pages'] == "":

            print()

            if request.POST['p_name']:
                newuser = Participant(
                    firstname = request.POST['p_name'],
                    password = request.POST['p_pass'],
                )
                newuser.save()
                print("[+] Created New USER: " + str(request.POST['p_name']))

            messages.success(request, 'Experiment is Over. Results have been saved successfully.')
            return redirect("homepage")        
        
        pages = request.POST['pages'].split(",")

        if request.POST['p_name'] != "nosubmit":
            newuser = Participant(
                firstname = request.POST['p_name'],
                password = request.POST['p_pass'],
            )
            newuser.save()
            print("[+] Created New USER: " + str(request.POST['p_name']))

        random_page = pages[randrange(len(pages))]
        pages.remove(random_page)
        context_dict = {}
        context_dict['remaining_pages'] = ','.join(map(str, pages))

        return render(request, random_page, context_dict)
    else:
        return HttpResponseBadRequest("Error. ")

def showDisplay(request, display_name):
    if display_name == "emoji":
        return render(request, "emoji.html")
    if display_name == "emojiandalpha":
        return render(request, "emojiandalpha.html")
    if display_name == "alpha":
        return render(request, "alphanumeric.html")
    
    
    return render(request, "homepage.html")


def showResults(request):
    results = Participant.objects.all()
    context_dict = {}
    context_dict['results'] = results
    return render(request, "results.html", context=context_dict)




