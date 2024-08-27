from django.db import models

# Create your models here.

class Category (models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250, blank=True)
    cat_img = models.ImageField(upload_to="photos/categories", blank=True)
    
    def __str__(self):
        return self.cat_name

class Product (models.Model):
   product_name = models.CharField(max_length=200, unique=True)
   description = models.TextField(max_length=500, blank=True)
   price = models.IntegerField()
   images = models.ImageField(upload_to="photos/products")
   stock = models.IntegerField()
   is_avilable = models.BooleanField(default=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
   
   def __str__(self):
        return self.product_name
