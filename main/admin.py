from django.contrib import admin
from .models import Profesor,Predmet
# Register your models here.
models_list = [Profesor,Predmet]

admin.site.register(models_list)