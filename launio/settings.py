import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kbe&e#9o$96%)qwo*z&w4ey_2*w=e)lk47#==_++cj!we6d=am'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG', 'False') == 'True'
DEBUG = False

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
ALLOWED_HOSTS = [
    '127.0.0.1:8000',
    'launio.herokuapp.com',
]
# TEMPLATE_DEBUG = DEBUG

# Application definition
DJANGO_APPS = ('django.contrib.admin',
               'django.contrib.auth',
               'django.contrib.contenttypes',
               'django.contrib.sessions',
               'django.contrib.messages',
               'django.contrib.staticfiles',
               # 'django.contrib.auth.models.User',
               )

THIRD_PARTY_APPS = ()

LA_UNIO_APPS = (
    'launio.club',
    'launio.accounts',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LA_UNIO_APPS

# end apps

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# AUTH_USER_MODEL = 'accounts.User'
# Auth User Model
AUTH_USER_MODEL = 'accounts.NewUser'

ROOT_URLCONF = 'launio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'launio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2mt9jipdphbfh',
        'USER': 'gzenihebnxhgon',
        'PASSWORD': 'c232f3554a135554eda834eb417ff83e1ede919ec3d7dbbce0b775e6459fcbb3',
        'HOST': 'ec2-52-30-67-143.eu-west-1.compute.amazonaws.com',
        'PORT': '5432'
    }
}

# 'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'club_db',
#     'USER': 'postgres',
#     'PASSWORD': '1234',
#     'HOST': '127.0.0.1',
#     'PORT': '5432',
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR_2, 'static'),
)
# STATICFILES_DIRS = (
#     BASE_DIR / "static",
# )
# STATIC_ROOT = BASE_DIR / 'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = 'home.html'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pakotestpako@gmail.com'
EMAIL_HOST_PASSWORD = 'TestTest2022'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
#
