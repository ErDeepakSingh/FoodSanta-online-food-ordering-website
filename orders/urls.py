from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.order_create,name='order_create'),
    url(r'^order_details/$',views.order_details,name='order_details'),
    url(r'^handlepayment/$',views.handlepayment,name='handlepayment'),

]