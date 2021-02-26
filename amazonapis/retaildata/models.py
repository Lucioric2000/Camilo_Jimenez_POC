from django.db import models

# Create your models here.
class RetailerAccount(models.Model):
    retailer = models.CharField(max_length=50)
    amazon_email = models.EmailField()
    amazon_password = models.CharField(max_length=40, help_text="Password, up to 40 characters")
    zipcode = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30)