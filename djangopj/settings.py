"""
Django settings for djangopj project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't600-6otf((3&!yg6&sa3zjaxyf-95zwa&i-i&wof2z#qvk*)+'

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
    'accounts',
    'calenders',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    
    'allauth',      
    'allauth.account',     
    'allauth.socialaccount',
    'django.contrib.sites',   
    "crispy_forms",
    'django_extensions',
    #'widget_tweaks',
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

ROOT_URLCONF = 'djangopj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[ 
                'bootstrap4.templatetags.bootstrap4',
            ],
        },
    },
]



WSGI_APPLICATION = 'djangopj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-db',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'db',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{"min_length":6},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.User'


AUTHENTICATION_BACKENDS = [ 
  'django.contrib.auth.backends.ModelBackend',     
  'allauth.account.auth_backends.AuthenticationBackend',
] 

SITE_ID = 1

#ユーザーネームは使わない
ACCOUNT_USERNAME_REQUIRED = False 
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#認証にはメールアドレスを使用する
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
#ログイン後のリダイレクト先を指定
LOGIN_REDIRECT_URL = reverse_lazy('nippo-list')
#ログアウト後のリダイレクト先
ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy("account_login")
#メールアドレスが確認済みである必要がある
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
#フォームに対して自動でBootstrapクラスを適用
CRISPY_TEMPLATE_PACK = 'bootstrap4'
#即時ログアウト
ACCOUNT_LOGOUT_ON_GET = True

BOOTSTRAP4 = {
    'include_jquery': True,
}

#メールをコンソールに表示する
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#実際に送信
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static_local" ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media_local"