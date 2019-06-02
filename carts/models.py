from django.db import models
from RESTAURANT.models import FoodDetails



class Cart(models.Model):
    products=models.ManyToManyField(FoodDetails,blank=True,null=True)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=True,auto_now=False)
    active=models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id %s"%(self.id)
