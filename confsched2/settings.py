"""
Django settings for confsched2 project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_DIRECTORY=os.path.join(BASE_DIR,'confsched2')+'/SECRET_KEY'
# SECURITY WARNING: keep the secret key used in production secret!
with open(SECRET_DIRECTORY) as f:
    SECRET_KEY = f.read().strip()


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'school.apps.SchoolConfig',
    'day.apps.DayConfig',
    'klass.apps.KlassConfig',
    'schedule.apps.ScheduleConfig',
    'student.apps.StudentConfig',
    'social_django', ## For django-social-auth
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', ## For django-social-auth
]

ROOT_URLCONF = 'confsched2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', ## For django-social-auth
                'social_django.context_processors.login_redirect', ## For django-social-auth
            ],
        },
    },
]

WSGI_APPLICATION = 'confsched2.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True

try:
    from confsched2.settings_local import *
except ImportError:
    pass
    
## For django-social-auth
SOCIAL_AUTH_POSTGRES_JSONFIELD = True
##SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_DIRECTORY=os.path.join(BASE_DIR,'confsched2')+'/OAUTH2_KEY'
# SECURITY WARNING: keep the secret key used in production secret!
with open(SECRET_DIRECTORY) as f:
	SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=f.readline().strip()
	SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=f.readline().strip()

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth', ## For django-social-auth
    'social_core.backends.google.GoogleOpenId', ## For django-social-auth
    'social_core.backends.google.GoogleOAuth2', ## For django-social-auth
    'social_core.backends.google.GoogleOAuth', ## For django-social-auth
    'django.contrib.auth.backends.ModelBackend',
)
