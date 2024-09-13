from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


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
    "december": None,
    
}

# Create your views here.

def monthly_cha_num(request, month):
    try:
        months = list(monthly_challengens.keys())
        foward_month = months[month - 1]
        foward_path = reverse("month-challenge", args=[foward_month])# /challenges/"month"
        return HttpResponseRedirect(foward_path)
    except:
        return HttpResponseNotFound("<h1>Error<h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challengens[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        response_data = render_to_string("404.html")
        raise Http404(response_data)


def home_page(request):
    months = list(monthly_challengens.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
        