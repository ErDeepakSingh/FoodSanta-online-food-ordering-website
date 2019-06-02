from django.db import models

class State(models.Model):
    state_name=models.CharField(max_length=25)
    def __str__(self):
        return self.state_name

class District(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    district_name=models.CharField(max_length=25)

    def __str__(self):
        return self.district_name


class Delivery_address(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address1=models.TextField(max_length=200)
    address2=models.TextField(max_length=200)
    district=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)

    def __str__(self):
        return 'Username: '+self.username+"--Email--: "+self.email