from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')

    def clean_email(self):
        email = self.cleaned_data['email']
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError("A client with this email already exists.")
        return email
