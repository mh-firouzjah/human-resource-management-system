"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as db_url
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    # django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # third party apps
    'jalali_date',
    'captcha',
    'admin_auto_filters',
    # 'modeltranslation',

    # local apps
    'apps.accounts.apps.AccountsConfig',
    'apps.BasicInformations.apps.BasicInformationsConfig',
    'apps.Garrisons.apps.GarrisonsConfig',
    'apps.Guards.apps.GuardsConfig',
    'apps.Stores.apps.StoresConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # translation
    'django.middleware.locale.LocaleMiddleware',
    # /translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# custom middlewares
MIDDLEWARE += [
    'apps.accounts.middleware.LoginRequiredMiddleware',
    'apps.accounts.middleware.PasswordValidationMiddleware',
    'apps.accounts.middleware.LoginFailedMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # translation
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {'default': db_url(config('DATABASES'))}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }, ]

AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = '/admin/login'
LOGIN_REDIRECT_URL = '/admin/'
# LOGIN_REQUIRED_IGNORE_PATHS = [ ]
LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [
    'admin:login', 'captcha-image', 'captcha-refresh'
]
LOGOUT_REDIRECT_URL = '/admin/login'

SESSION_SAVE_EVERY_REQUEST = True  # to reset the SESSION_EXPIRY
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 700 * 60  # SESSION_EXPIRY in seconds

PASSWORD_EXPIRE_INTERVAL_DAYS = 45

LOGIN_FAILED_LIMIT = 3
LOGIN_FAILED_COOLDOWN = (5 * 60)  # seconds

CAPTCHA_IMAGE_SIZE = [150, 38]
CAPTCHA_FONT_SIZE = 22
CAPTCHA_CHALLENGE_FUNCT = 'apps.accounts.utils.captcha'
CAPTCHA_LENGTH = 4
CAPTCHA_STRING_CASESENSITIVE = True

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# try:
#     import locale
#     locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
# except Exception:
#     pass

LOCALE_PATHS = [BASE_DIR / 'locale', ]
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fa'
# translation
LANGUAGES = [
    ('en', _('English')),
    ('fa', _('Persian')),
]
# /translation


# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / "assets",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}
