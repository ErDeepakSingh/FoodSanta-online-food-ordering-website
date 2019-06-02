from django.contrib import admin
from . import models as delivery_models
# Register your models here.
admin.site.register(delivery_models.State)
admin.site.register(delivery_models.District)
admin.site.register(delivery_models.Delivery_address)