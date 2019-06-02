from django.db import models
from ACCOUNTS.models import User


class Add_Restaurant(models.Model):
    rest_author=models.ForeignKey(User,on_delete=models.CASCADE)
    rest_title=models.CharField(max_length=150)
    rest_created=models.DateTimeField(auto_now_add=True)
    rest_image=models.ImageField(default='default.png',upload_to='restaurant_image')
    rest_desc=models.TextField(max_length=1000)
    locality=models.CharField(max_length=255,default='')
    city=models.CharField(max_length=255,default='')
    pincode=models.CharField(max_length=10,default='')

    def __str__(self):
        return self.rest_title+self.rest_created.strftime('%d-%m-%y')
class FoodDetails(models.Model):
    rest=models.ForeignKey(Add_Restaurant,on_delete=models.CASCADE)
    food_title=models.CharField(max_length=50)
    food_cuisine=models.CharField(max_length=50)
    food_image=models.ImageField(default='food.png',upload_to='food_images')
    food_price = models.CharField(max_length=50)
    food_Description = models.TextField(max_length=200)

    def __str__(self):
        return "Food :"+self.food_title+"- Cuisine-"+self.food_cuisine
    def short_desc(self):
        desc=self.food_Description.split('.')
        return desc[0]

# class District(models.Model):
#     state = models.ForeignKey(State,
#                               on_delete=models.CASCADE)
#     dist_name = models.CharField(max_length=25)
#
#     def __str__(self):
#         # return self.dist_name+"- "+self.state.state_name
#         return self.dist_name
