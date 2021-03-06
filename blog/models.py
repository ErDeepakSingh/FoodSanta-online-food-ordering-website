from django.db import models
from django.utils import timezone
from ACCOUNTS.models import User
from django.urls import reverse
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str_(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('Blog_home',kwargs={'pk':self.pk})