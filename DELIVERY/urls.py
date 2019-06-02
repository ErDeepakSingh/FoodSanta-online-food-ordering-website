from django.conf.urls import url
from . import views as delivery_views

urlpatterns=[
    url(r"^$",delivery_views.delivery_home,name='delivery_home'),
    url(r"^state/",delivery_views.delivery_state,name='delivery_state'),
    url(r"^delivery_address/",delivery_views.add_delivery_address,name='add_delivery_address')
]