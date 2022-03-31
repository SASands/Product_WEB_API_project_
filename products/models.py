from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_quantity = models.IntegerField
    product_image = models.TextField(max_length=1000, default= '')



  