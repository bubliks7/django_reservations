from django import forms
from appointments.models import Rezerwacja

class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = ['data_od', 'data_do']
        widgets = {
            'data_od': forms.DateInput(attrs={'type': 'date'}),
            'data_do': forms.DateInput(attrs={'type': 'date'}),
        }
