from django.shortcuts import render
from django.conf import settings
import os
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
#from .models import UserSettings
#from .forms import SettingsForm
from django.template import loader


# Create your views here.
class RetailerAddView(LoginRequiredMixin, View):
    def get(self, request):
        settingsobj = SettingsView.get_existent_or_default_settings(request)
        #return HttpResponse(f"Variables.py placeholder for {request.user.is_authenticated}")
        context = {"usersettings": settingsobj, "interval_times_60000": settingsobj.interval * 60000,
                   "color_change_interval": settingsobj.color_change_interval}
        return render(request, os.path.join("cryptoorchid", "variables.py"), context=context)

class VariablesPyHtmlView(LoginRequiredMixin, View):
    """A variables.py version that displays OK in web browsers"""
    def get(self, request):
        settingsobj = SettingsView.get_existent_or_default_settings(request)
        t = loader.get_template(os.path.join("cryptoorchid", "variables.py"))
        context = {"usersettings": settingsobj, "interval_times_60000": settingsobj.interval * 60000,
                   "color_change_interval": settingsobj.color_change_interval}
        templatedstring = t.render(context, request)#.replace("\n", "<br/>\n")
        return HttpResponse(f"<pre>{templatedstring}</pre>", content_type='text/html')
