from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from requests import request

from accounts.manager import UserManager
from django.db.models.signals import pre_save
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_log_out = models.DateTimeField(null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    



@receiver(pre_save,sender=User)
def getusername(sender,instance,*args, **kwargs):
    print("hellow")
    
    





