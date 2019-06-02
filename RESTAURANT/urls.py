from django.conf.urls import url
from . import views as restaurant_views

urlpatterns=[
    url(r'^$',restaurant_views.restaurant_home,name='restaurant_home'),
    url(r'^add-restaurant/$',restaurant_views.add_restaurant,name='add_restaurant'),
    url(r'^add_food/$',restaurant_views.add_food,name='add_food'),
    url(r'^(?P<rest_id>\d+)/(?P<food_id>\d+)/$',restaurant_views.food_details,name='food_details'),
    url(r'^(?P<rest_id>\d+)/$',restaurant_views.restaurant_details,name='restaurant_details'),
]