# -*- coding: utf-8 -*-
"""
Django settings for coffeehouse project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG # default INFO

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kcs+%f+q_^qzf_u@^lol#(uv-h*=_r)-*&62_h&_6#7=lnh=d7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#The purpose of ALLOWED_HOSTS is to validate a request’s HTTP Host header.
ALLOWED_HOSTS = [
    '192.168.1.80',
    '.coffeehouse.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coffeehouse.about',
    'coffeehouse.stores',
    'coffeehouse.jj2app',
    'coffeehouse.registration',
#    'coffeehouse.jj2app.apps.Jj2appConfig',
    'debug_toolbar',
    # Django sites app  required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',
]
#SOCIALACCOUNT_PROVIDERS = {'facebook': {}, 'google':{}, 'twitter':{}}

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coffeehouse.urls'

#print('jinja2 tpl path: %s/jinja2tpl/' % PROJECT_DIR)

TEMPLATES = [
    {
        'NAME': 'JINJA2',
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': ['%s/jinja2/' % (PROJECT_DIR),],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'coffeehouse.jinja2.env.JinjaEnvironment',
            #'autoescape': False,
            #'cache_size': 400, # default size of template cached.
            #'undefined': Jinja2.StrictUndefined,   #ERROR
        }
    },
    {
        'NAME': 'DJANGO',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['%s/templates/' % PROJECT_DIR],
        # The APP_DIRS variable set to True tells Django to look for templates in Django app subfolders named templates
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'autoescape': True,
            'context_processors': [
                #  context processor offers the ability to share data across all Django templates, without the need to define it in a piecemeal fashion in Django views
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coffeehouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '192.168.1.5',
        'PORT': '5432',
        'NAME': 'django_demo',
        'USER': 'postgres',
        'PASSWORD':'postgres',
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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
    #'/var/www/static/',
]

# django-debug-toolbar 设置
#INTERNAL_IPS = ('127.0.0.1','192.168.1.5') #允许这些IP访问时显示debug-toolbar.
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_CONFIG = {
    #'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js',
    'JQUERY_URL': '//apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js',
}

# 日志设置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s.%(msecs)03d] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '/tmp/django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/django_production.log',
            'maxBytes' : 1024*1024*100, # 100MB
            'backupCount' : 5,
            'formatter': 'simple'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false','require_debug_true'],
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/dba.log',
            'formatter': 'simple'
        },
    },
    'root': {
        'level': 'DEBUG',
        #'level': 'WARNING',
        'handlers': ['console'],
    },
    'loggers': {
        'coffeehouse': {
            'handlers': ['development_logfile','production_logfile'],
         },
        'dba': {
            'handlers': ['dba_logfile'],
        },
        'django': {
            'handlers': ['development_logfile','production_logfile'],
        },
        'py.warnings': {
            'handlers': ['development_logfile'],
        },
    }
}

# 配置自定义用户表
AUTH_USER_MODEL = 'registration.CoffeehouseUser'

# Ensure SITE_ID is set sites app
SITE_ID = 1
# Add the 'allauth' backend to AUTHENTICATION_BACKEND and keep default ModelBackend
AUTHENTICATION_BACKENDS = [ 'django.contrib.auth.backends.ModelBackend',
                           'allauth.account.auth_backends.AuthenticationBackend']
# EMAIL_BACKEND so allauth can proceed to send confirmation emails
# ONLY for development/testing use console
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

