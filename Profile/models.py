from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    short_details=models.TextField()
    quantity=models.PositiveIntegerField()
    prod_img=models.ImageField(upload_to='product_img/')
    sub_prod_img1=models.ImageField(upload_to='product_img/sub_prod_img/')
    sub_prod_img2=models.ImageField(upload_to='product_img/sub_prod_img/')
    sub_prod_img3=models.ImageField(upload_to='product_img/sub_prod_img/')
    description=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    featured_prod=models.BooleanField(default=False)
    New_arrivals=models.BooleanField(default=False)
    Best_selling_prod=models.BooleanField(default=False)

    def __str__(self):
        return self.name