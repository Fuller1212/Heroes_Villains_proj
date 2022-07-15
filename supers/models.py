from django.db import models
from django.forms import CharField

# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    second_ability = models.CharField(max_length=255)