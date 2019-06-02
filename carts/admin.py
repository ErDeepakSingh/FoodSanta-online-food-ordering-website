from django.contrib import admin
from . import models as Cart_models

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model=Cart_models.Cart
admin.site.register(Cart_models.Cart,CartAdmin)