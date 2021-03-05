from django.shortcuts import render
from django.conf import settings
import os
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .import models
from .forms import RetailerForm, GiftCodeForm
from django.template import loader
from .scripts import amazoncall

# Create your views here.
class RetailerAddView(View):

    def get(self, request):
        rfrm = RetailerForm()
        return render(request, 'retaildata/retailer.html', {'form': rfrm})

    def post(self, request):
        rfrm = RetailerForm(request.POST)
        if rfrm.is_valid():
            sc = rfrm.clean()
            saved = rfrm.save()
            messages.success(request, "The dashboard configuration was saved.")
            rfrm = RetailerForm()
        else:
            messages.error(request, "An error were found. Check the values above.")
        return render(request, 'retaildata/retailer.html', {'form': rfrm})


class StatusesView(ListView):
	#by default it loads from retaildata/coderedemption_list.html
	model = models.CodeRedemption

class AmazonAccountsView(ListView):
	model = models.RetailerAccount

class QuickRedeemView(View):
    template_name = 'retaildata/quick_redeem.html'
    def get(self, request):
        rfrm = GiftCodeForm()
        return render(request, self.template_name, {'form': rfrm})

    def post(self, request):
        rfrm = GiftCodeForm(request.POST)
        if rfrm.is_valid():
            sc = rfrm.clean()
            accountkeys = sc["account"].split(" at ")#retailer and then amazon-email. preparing for the coumpund key between these fields
            redemptionaccount = models.RetailerAccount.objects.get(retailer=accountkeys[1], amazon_email=accountkeys[0])
            params = {"gift_code": sc["gift_code"], "account_where_to_redeem": redemptionaccount}
            finder = models.CodeRedemption.objects.filter(**params)
            if len(finder):
                codeobj = finder.get()
            else:
                codeobj = models.CodeRedemption.objects.create(**params)
                codeobj.save()
            try:
                gcs = amazoncall.GiftCodeScraper(codeobj, False)
            except Exception as exc:
                #raise
                messages.error(request, f"Error {exc} when redeeming the gift code. Redemption added to the queue.")
            else:
                messages.success(request, f"The gift code was tested for redemption with result {codeobj.status}.")
            rfrm = GiftCodeForm()
        else:
            messages.error(request, "One or more errors were found.")
        return render(request, self.template_name, {'form': rfrm})


class RedeemView(View):
    """This class stands for the unimplemented case that the code is only saved to be redemed later."""
    template_name = 'retaildata/redeem.html'
    def get(self, request):
        rfrm = GiftCodeForm()
        return render(request, self.template_name, {'form': rfrm})

    def post(self, request):
        rfrm = GiftCodeForm(request.POST)
        if rfrm.is_valid():
            sc = rfrm.clean()
            accountkeys = sc["account"].split(" at ")#retailer and then amazon-email. preparing for the coumpund key between these fields
            redemptionaccount = models.RetailerAccount.objects.get(retailer=accountkeys[1], amazon_email=accountkeys[0])
            params = {"gift_code": sc["gift_code"], "account_where_to_redeem": redemptionaccount}
            finder = models.CodeRedemption.objects.filter(**params)
            if len(finder):
                codeobj = finder.get()
                messages.info(request, "The gift code was already saved to the redemption queue to the selected Amazon account")
            else:
                codeobj = models.CodeRedemption.objects.create(**params)
                codeobj.save()
                messages.success(request, "The gift code was saved to the redemption queue.")
            rfrm = GiftCodeForm()
        else:
            messages.error(request, "One or more errors were found.")
        return render(request, self.template_name, {'form': rfrm})

class ClearView(View):
    template_name = 'retaildata/clear.html'
    def get(self, request):
        for database in (models.RetailerAccount, models.CodeRedemption):
            try:
                database.objects.all().delete()
                #database.save()
            except Exception as exc:
                raise exc
                return render(request, self.template_name, {'message': f'The error {exc} happened when trying to clear the database table {database}.'})
        else:
            return render(request, self.template_name, {'message': 'The database tables were cleared.'})
