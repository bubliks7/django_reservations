from django import forms
from appointments.models import Opinia

class opinionForm(forms.ModelForm):
    class Meta:
        model = Opinia
        fields = ['ocena', 'comment']
        widgets = {
            'ocena': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(),
        }
