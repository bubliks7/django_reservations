from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

class Samochod(models.Model):
    id = models.AutoField(primary_key=True)
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    rok = models.IntegerField()
    cena_za_dzien = models.DecimalField(max_digits=8, decimal_places=2)
    opis = models.TextField()
    zdjecie = models.ImageField(upload_to='cars/', blank=True, null=True)

    def dostepny(self, data_od, data_do):
        return not self.rezerwacje.filter(
            status='confirmed',
            data_od__lt=data_do,
            data_do__gt=data_od
        ).exists()

    def __str__(self):
        return f"{self.marka} - {self.model} - {self.rok}"
    
class Rezerwacja(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekuje'),
        ('confirmed', 'Potwierdzona'),
        ('cancelled', 'Anulowana'),
    ]
    id = models.AutoField(primary_key=True)
    klient = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Samochod, on_delete=models.CASCADE, related_name='rezerwacje')
    data_od = models.DateField()
    data_do = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cena_ogolna = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.data_od >= self.data_do:
            raise ValidationError("Data zakonczenia musi byc pozniej niz data rozpoczecia")

        if self.data_od < date.today():
            raise ValidationError("Nie rezerwuj w przeszlosci")
        
        if not self.auto.dostepny(self.data_od, self.data_do):
            raise ValidationError("Auto niedostepne w wybranym terminie")

    def save(self, *args, **kwargs):
        self.full_clean()
        dni = (self.data_do - self.data_od).days
        self.cena_ogolna = dni * self.auto.cena_za_dzien
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.auto} - {self.data_od} - {self.data_do}"
