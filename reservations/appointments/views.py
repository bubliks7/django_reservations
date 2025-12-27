from django.shortcuts import render, get_object_or_404, redirect
from .models import Samochod

def home(request):
    auta = Samochod.objects.all()[:3]
    return render(request, 'appointments/homePage.html', {'auta': auta})

def allCars(request):
    auta = Samochod.objects.all()
    return render(request, 'appointments/allCars.html', {'auta': auta})

def seeMore(request, pk):
    auta = get_object_or_404(Samochod, pk=pk)
    return render(request, "appointments/seeMore.html", {'auta': auta})
