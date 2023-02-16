from django.shortcuts import render, redirect
from random import randrange
from hcs_app.models import Participant
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

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


@csrf_exempt
def checkPasswordStrength(request):
    if request.method == "POST":
        print(request.POST)
        hrs = timeToCrack(request.POST['password'])
        hrs = float(hrs)
        return HttpResponse(hrs,
            content_type="application/json")
    return HttpResponse(status=404)

    

# calculate smaple space of one character of a password
def charSpace(letter, used):
    if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
        used["lower"] = True
        return used
    elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        used["upper"] = True
        return used
    elif letter in ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''':
        used["num"] = True
        return used
    elif letter in "0123456789":
        used["char"] = True
        return used
    elif letter in "😀😊😅😂🙂😉😍😛😠😎😏😬😭😓😱😪😬😴😯😐😇🤣😘😚😆😡😥😓🙄":
        used["emo"] = True
        return used



# calculate password sample space
def pwordSpace(pword):
    used = {"lower": False, "upper": False, "num": False, "char": False, "emo": False}
    for letter in pword:
        used = charSpace(letter, used)

    pwordSpace = 0

    if used["lower"]:
        pwordSpace += 26
    if used["upper"]:
        pwordSpace += 26
    if used["num"]:
        pwordSpace += 10
    if used["char"]:
        pwordSpace += 33
    if used["emo"]:
        pwordSpace += 29
            
    
    return pwordSpace ** len(pword)


# calculate time to crack a password(estimate)
def timeToCrack(pword):
    sampleSpace = pwordSpace(pword)

    # number of effective cores on a machine = 1/((1-Efficiency Constant)+(Efficiency Constant/Processor Cores))
    # assume efficiency constant to be 0.5 - 50% of CPU power can go towards password cracking
    # assume 12 cores, 5GHz - according to Intel Core I7-12700K
    effCores = 1/((1 - 0.5) + (0.5/12))

    # number of floating point operations per second (in billions)
    gflops = effCores * 5

    seconds_to_crack = sampleSpace/(gflops * 10**9)
    hours_to_crack = seconds_to_crack/3600

    #print("It would take ", years_to_crack, " hours to crack this password.")
    return hours_to_crack






