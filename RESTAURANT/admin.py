from django.contrib import admin
from . import models as rest_models
# Register your models here.
admin.site.register(rest_models.Add_Restaurant)
admin.site.register(rest_models.FoodDetails)