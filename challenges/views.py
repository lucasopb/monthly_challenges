from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challengens = {
    "january": "walk",
    "february": "run",
    "march": "swin",
    "april": "work out",
    "may": "eat",
    "june": "play with the dog",
    "july": "jump",
    "august": "play soccer",
    "september": "dance",
    "october": "talk with mom",
    "november": "rest",
    "december": "pray",
    
}

# Create your views here.

def monthly_cha_num(request, month):
    try:
        months = list(monthly_challengens.keys())
        foward_month = months[month - 1]
        foward_path = reverse("month-challenge", args=[foward_month])# /challenges/"month"
        return HttpResponseRedirect(foward_path)
    except:
        return HttpResponseNotFound("<h1>error<h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challengens[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>error<h1>")


def home_page(request):
    list_itens = ""
    months = list(monthly_challengens.keys())
    for month in months:
        foward_path = reverse("month-challenge", args=[month])
        list_itens += f"<li><a href={foward_path}>{month.capitalize()}</a></li>"
        
    return HttpResponse(f"<ul>{list_itens}</ul>")
        