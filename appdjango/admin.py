from multiprocessing import managers
from django.contrib import admin
from .models import a
# from django.contrib.admin import site,register
# Register your models here.
admin.site.register(a)
