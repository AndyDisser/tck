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
        einzelbuchung = Trainingsangebot.objects.filter(category="Einzeln")
        abo = Trainingsangebot.objects.filter(category="Abo")
        camp = Trainingsangebot.objects.filter(category="Camp")
    }
    print(f"\n\n{Trainingsangebot}\n{einzelbuchung}\n{abo}\n{camp}\n\n")
    return render(request, "home/training.html", context)
