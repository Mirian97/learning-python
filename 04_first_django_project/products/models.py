from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=255, null=True)
    price= models.FloatField(default=0)
    stock= models.IntegerField(default=0)
    image= models.CharField(max_length=2083, null=True)
    
class Offer(models.Model):
    code= models.CharField(max_length=10, null=True)
    description = models.TextField(max_length=255, null=True)
    discount = models.FloatField(default=0)