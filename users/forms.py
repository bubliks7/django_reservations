from django import forms
from django.contrib.auth.models import User

class RejestracjaForm(forms.Form):
    login = forms.CharField(max_length=150, label='Nazwa użytkownika')
    haslo = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    potwierdz_haslo = forms.CharField(widget=forms.PasswordInput, label="Potwierdź hasło")
    imie = forms.CharField(max_length=75, label='Imię')
    nazwisko = forms.CharField(max_length=80, label='Nazwisko')
    email = forms.EmailField(label='Email')
    
    def clean(self):
        cleaned_data = super().clean()
        haslo = cleaned_data.get('haslo')
        potwierdz_haslo = cleaned_data.get('potwierdz_haslo')

        if haslo != potwierdz_haslo:
            raise forms.ValidationError('Hasla musza byc takie same')
        return cleaned_data

    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data['login'],
            password=self.cleaned_data['haslo'],
            first_name=self.cleaned_data['imie'],
            last_name=self.cleaned_data['nazwisko'],
            email=self.cleaned_data['email']
        )
