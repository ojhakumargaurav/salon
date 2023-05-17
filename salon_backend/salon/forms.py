from django import forms
from django.forms import ModelForm, TextInput, EmailInput, SelectDateWidget, TimeInput
from .models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'service', 'date', 'time']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your name'}),
            'email': EmailInput(attrs={'placeholder': 'Your email'}),
            'date': SelectDateWidget(),
            'time': TimeInput(),
        }
