from django.db import models
from django import forms# import ModelForm
from .models import RetailerAccount

		#assert 0,dir()
class RetailerForm(forms.ModelForm):
    class Meta:
        model = RetailerAccount
        exclude = ()