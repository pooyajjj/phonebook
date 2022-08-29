from pyexpat import model
from django.db import models

# Create your models here.

class phonenum(models.Model):
    name = models.CharField(max_length = 200)
    phone_num = models.CharField (max_length = 11)