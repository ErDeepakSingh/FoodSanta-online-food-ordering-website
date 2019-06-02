from django.conf.urls import url
from . import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns=[

    url(r'^contact_us/$', accounts_views.contact_us, name='contact_us'),
    url(r'^signup/$', accounts_views.SignUpView.as_view(), name='signup'),
    url(r'^signup/customer/$', accounts_views.CustomerSignUpView.as_view(), name='customer_register'),
    url(r'^signup/vendor/$', accounts_views.VendorSignUpView.as_view(), name='vendor_register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^profile/$', accounts_views.profile,name='profile'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    # url(r'^new/$', views.PostCreateView.as_view(), name='Blog_create'),
    url(r'^password_reset/$',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    url(r'^password_reset/done$',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^password_reset-confirm/(?P<uidb64>[0-9A-'
    r'Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^password_reset_complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    url(r'^password_change/$',
        auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html'),name='password_change'),
    url(r'^password_change/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),

]