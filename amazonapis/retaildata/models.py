from django.db import models

# Create your models here.
class RetailerAccount(models.Model):
    retailer = models.CharField(max_length=50)
    amazon_email = models.EmailField(primary_key=True)
    amazon_password = models.CharField(max_length=100, help_text="Password, up to 40 characters")
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30)
    def email_and_retailer(self):
    	return f"{self.amazon_email} at {self.retailer}"

class CodeRedemption(models.Model):
	gift_code = models.CharField(max_length=50, primary_key=True)
	account_where_to_redeem = models.ForeignKey(RetailerAccount, on_delete=models.CASCADE)
	redemption_date = models.DateTimeField(null=True)
	status = models.BooleanField(null=True)
	status_message = models.TextField(null=True, blank=True)