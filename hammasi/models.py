from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('s','author'),
        ('t','book')
    )

    USERNAME_FIELD = 'username'
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

# Create your models here.


class car(models.Model):
    name = models.CharField(max_length=20,default='')
    color = models.CharField(max_length=10,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    motor = models.CharField(max_length=100)
    information = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CAR'


class car_shop(models.Model):
    name = models.CharField(max_length=70,default='')
    address = models.CharField(max_length=70,default='')
    car_name = models.CharField(max_length=70,default='')
