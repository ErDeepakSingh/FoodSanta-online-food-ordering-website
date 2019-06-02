from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .signals import create_user_profile,save_user_profile
class UsersConfig(AppConfig):
    name = 'accounts'

    # def ready(self):
    #     import accounts.signals

    def ready(self):
        post_save.connect(create_user_profile, sender=User)
        post_save.connect(save_user_profile, sender=User)
