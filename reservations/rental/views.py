from django.shortcuts import render, get_object_or_404, redirect
from appointments.models import Samochod, Rezerwacja
from django.contrib.auth.decorators import login_required
from .forms import RezerwacjaForm
from django.contrib import messages
# Create your views here.

@login_required
def rezerwuj(request, pk):
    auto = get_object_or_404(Samochod, pk=pk)

    if request.method == 'POST':
        form = RezerwacjaForm(request.POST)
        form.instance.auto = auto # inaczej wywala blad
        if form.is_valid():
            rezerwacja = form.save(commit=False)
            rezerwacja.klient = request.user
            rezerwacja.auto = auto
            rezerwacja.save()
            return redirect('/rental/myReservations/')
    else:
        form = RezerwacjaForm()

    return render(request, 'rental/create.html', {'form': form, 'auto': auto})

@login_required
def mojeRezerwacje(request):
    rezerwacje = Rezerwacja.objects.filter(klient=request.user)
    return render(request, "rental/myReservations.html", {'rezerwacje': rezerwacje})

@login_required
def anulujRezerwacje(request, pk):
    if request.method == "POST":
        rezerwacje = get_object_or_404(Rezerwacja, pk=pk, klient=request.user)
        if rezerwacje.status == "confirmed":
            messages.error(request, "Rezerwacja jest już zatwierdzona, nie możesz jej anulować!")
        else:
            rezerwacje.status = 'cancelled'
            rezerwacje.save()

    return redirect('rental:mojeRezerwacje')
