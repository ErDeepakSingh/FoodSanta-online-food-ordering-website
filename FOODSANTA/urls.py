from django.conf.urls import (url,
                              include)
from django.contrib import admin
from . import views as food_santa_views
from . import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', food_santa_views.food_santa_home,name='food_santa_home'),
    url(r'^s/$', food_santa_views.search,name='search'),
    url(r'^about_us/', food_santa_views.about_us,name='about_us'),
    url(r'accounts/',include('ACCOUNTS.urls')),
    url(r'restaurant/',include('RESTAURANT.urls')),
    url(r'delivery/',include('DELIVERY.urls')),
    url(r'carts/',include('carts.urls')),
    url(r'blog/',include('blog.urls')),
    url(r'orders/',include('orders.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
