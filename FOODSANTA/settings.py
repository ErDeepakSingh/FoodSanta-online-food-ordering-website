"""
Django settings for FOODSANTA project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from . conf import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3tpfqg^@dxhnh(61-)(es*87wpn5sm2f_u68m(=vcq_mh6e^n9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ACCOUNTS',
    'RESTAURANT',
    'DELIVERY',
    'blog',
    'carts',
    'crispy_forms',
    'orders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FOODSANTA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carts.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'FOODSANTA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'foodsantadb',
#         'USER': 'postgres',
#         'PASSWORD': 'pass@123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodsanta',
        'USER': 'root',
        'PASSWORD': 'Deepak@1997',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'ACCOUNTS.User'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_REDIRECT_URL='food_santa_home'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')
MEDIA_URL='/restaurant_image/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "post_image"),
    os.path.join(BASE_DIR, "accounts"),
]
CRISPY_TEMPLATE_PACK='bootstrap4'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=myemail
EMAIL_HOST_PASSWORD=mypassword
CART_SESSION_ID='cart'

#django-paypalsettings
# PAYPAL_RECIEVER_EMAIL='deepakthakur755@gmail.com'
# PAYPAL_TEST=True
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
