from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "birthdate",
            "email",
            "password",
        ]
        labels = {
            "first_name": _("Vorname"),
            "last_name": _("Nachname"),
            "username": "Benutzername",
            "birthdate": "Geburtsdatum",
            "email": "E-Mail Adresse",
            "password": "Passwort",
        }
        help_texts = {"username": ""}
        error_messages = {"name": {"required": "Pflichtfeld"}}

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label="Benutzername")
    password = forms.CharField(widget=forms.PasswordInput, label="Passwort")
