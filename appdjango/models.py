from django.db import models
from django.forms import CharField

# Create your models here.
class a(models.Model):
    name=models.CharField(max_length=17)

    def __str__(self):
            return  self.name[0:3]+'...'