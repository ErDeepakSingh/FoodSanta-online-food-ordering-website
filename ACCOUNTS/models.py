from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    is_vendor = models.BooleanField('Vendor status', default=False)
    is_customer = models.BooleanField('Customer status', default=False)
    def __str__(self):
        return str(self.id)+":-"+self.username


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)


class Contact(models.Model):
    name=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    message=models.TextField(max_length=500)
    recieved = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.email
