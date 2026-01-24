from django.contrib import admin
from .models import Rezerwacja, Samochod, Opinia
# Register your models here.

admin.site.register(Samochod)
admin.site.register(Rezerwacja)
admin.site.register(Opinia)
