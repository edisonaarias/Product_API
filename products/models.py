from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.IntegerField()
    description = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.CharField(max_length=255)
