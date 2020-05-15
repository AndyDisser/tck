from django.shortcuts import render, redirect
from .models import Trainingsangebot

def index(request):
    context = {

    }
    return render(request, "home/index.html", context)

def mannschaften(request):
    context = {

    }
    return render(request, "home/mannschaften.html", context)

def mannschaft(request, mannschaft):
    context = {
        "mannschaft": mannschaft
    }
    return render(request, "home/mannschaft.html", context)

def training(request):
    context = {
        "einzelbuchung" : Trainingsangebot.objects.filter(category="Einzeln").all(),
        "abo" : Trainingsangebot.objects.filter(category="Abo").all(),
        "camp" : Trainingsangebot.objects.filter(category="Camp").all()
    }
    return render(request, "home/training.html", context)

def feldherrnhuegel(request):
    context = {

    }
    return render(request, "home/feldherrnhuegel.html", context)
