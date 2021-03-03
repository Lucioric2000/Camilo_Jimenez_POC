from django.shortcuts import render
from django.conf import settings
import os
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
#from .models import UserSettings
from .forms import RetailerForm
from django.template import loader


# Create your views here.
#class RetailerAddView(LoginRequiredMixin, View):
class RetailerAddView(View):
    def get(self, request):
        rfrm = RetailerForm()
        #return render(request, os.path.join("cryptoorchid", "variables.py"), context=context)
        return render(request, 'retaildata/retailer.html', {'form': rfrm})
