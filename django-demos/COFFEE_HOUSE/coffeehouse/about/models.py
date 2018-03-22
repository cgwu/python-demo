from django.db import models
from django import forms

# Create your models here.


# Forms.
class ContactForm(forms.Form):
    name = forms.CharField(required=False, initial='Please provide your name')
    email = forms.EmailField(label='Your email', initial='We need your email')
    comment = forms.CharField(widget=forms.Textarea)

