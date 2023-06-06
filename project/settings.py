"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path
from configurations import Configuration, values


class Base(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition

    INSTALLED_APPS = [
        "authentication.apps.AuthenticationConfig",
        "feeds.apps.FeedsConfig",
        "commentary.apps.CommentaryConfig",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],
    }

    ROOT_URLCONF = "project.urls"

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATIC_URL = "static/"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [STATIC_ROOT],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "project.wsgi.application"

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.1/topics/i18n/

    LANGUAGE_CODE = "de"
    LANGUAGES = [("de", "deutsch"), ("en", "english"), ("fr", "français")]
    LOCALE_PATHS = [BASE_DIR / "project/locale"]

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AUTH_USER_MODEL = "authentication.User"
    LOGIN_URL = "/login"
    LOGIN_REDIRECT_URL = ""

    TEST_RUNNER = "django.test.runner.DiscoverRunner"
    TEST_DISCOVER_TOP_LEVEL = "*"
    TEST_DISCOVER_PATTERN = "tests/*.py"


class Development(Base):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = "django-insecure-uu$jxlvcp$b34*mv*ylla(dn6ls=ro40t_1!f3mb!z+%4_=_a&"

    DEBUG = True

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'feeder_database',
            'USER': 'feeder_db_admin',
            'PASSWORD': 'pw_feeder.db',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


class Production(Base):
    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {

        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'feeder_database',
            'USER': 'feeder_db_admin',
            'PASSWORD': 'pw_feeder.db',
            'HOST': 'db',
            'PORT': '5432',
        }
    }


class Testing(Development):
    pass
