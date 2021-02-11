from django.db import models
from ecommerce_app.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='Cart',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.user.username


