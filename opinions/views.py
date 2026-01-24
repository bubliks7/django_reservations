from django.shortcuts import render
from appointments.models import Opinia
# Create your views here.

def viewOpinions(request):
    opinions = Opinia.objects.all()
    return render(request, 'opinions/opinie.html', {'opinions': opinions})
