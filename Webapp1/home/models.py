from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    point = models.PositiveIntegerField(default = 10000)
    
class Pointusing(models.Model):
    user = models.CharField(max_length = 255)
    time = models.DateTimeField(verbose_name="日時",default=timezone.now)
    goods = models.CharField(max_length = 255)
    quantity  = models.PositiveIntegerField(null=False,blank=False) 
    point = models.PositiveIntegerField(null=False,blank=False)


class Shopinfo(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField(max_length=200)
    #shop_pic=models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.name