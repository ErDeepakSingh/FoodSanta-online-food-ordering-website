from django.conf.urls import url
from . import views as cart_views

urlpatterns=[
    url(r'^$',cart_views.cart_detail,name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$',cart_views.cart_add,name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$',cart_views.cart_remove,name='cart_remove'),
]
# r'^(?P<rest_id>\d+)/$'