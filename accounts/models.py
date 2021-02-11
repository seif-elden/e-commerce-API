from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Governorates(models.Model):
    governorate = models.CharField(max_length=50)

    def __str__(self):
        return self.governorate
    


class Cities_of_governorates(models.Model):
    governorate = models.ForeignKey(Governorates,related_name='city',on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    def __str__(self):
        return self.city
   

class Address(models.Model):
    user = models.ForeignKey(User,related_name='Address',on_delete=models.CASCADE) 
    city = models.ForeignKey(Cities_of_governorates,related_name='adress',on_delete=models.CASCADE)
    destrict = models.CharField(max_length=50) 
    street = models.CharField(max_length=50)
    building_number = models.CharField(max_length=5 )
    floor = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.user.username} | {self.pk}'

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
