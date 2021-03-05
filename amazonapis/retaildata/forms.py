from django.db import models
from django import forms# import ModelForm
from .models import RetailerAccount

		#assert 0,dir()
class RetailerForm(forms.ModelForm):
    class Meta:
        model = RetailerAccount
        exclude = ()

class GiftCodeForm(forms.Form):
	account = forms.ChoiceField(choices=[(obj.email_and_retailer(), obj.email_and_retailer()) for obj in RetailerAccount.objects.all()])
	gift_code = forms.CharField(max_length=100)
	def __init__(self, *args, **kwargs):
		super(__class__, self).__init__(*args, **kwargs)
		print("instantiating", __class__)
		#assert 0, list(self)
		self.fields["account"].choices = [(obj.email_and_retailer(), obj.email_and_retailer()) for obj in RetailerAccount.objects.all()]