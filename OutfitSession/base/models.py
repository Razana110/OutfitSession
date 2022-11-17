from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)

    REQUIRED_FIELDS = []



class DT_model(models.Model):
    desiger = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateField(null = True)
    time = models.TimeField(null = True)
    status = models.BooleanField(default = None, null = True)
    email = models.EmailField(null=True)

    def __str__(self):
        return "Dt: " + str(self.desiger)



class Connect_Model(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.email)