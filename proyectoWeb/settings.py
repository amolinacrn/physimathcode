"""
Django settings for proyectoWeb project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from django.conf import settings
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-pdion^t*fyk8mzv_8a65^oq6nzdz21cot_dzpw#sjlg#auq99w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "sorl.thumbnail",
    "physimathcode",
    "cursos",
    "fisicalab1",
    "fisicalab2",
    "autenticacion",
    "classroom",
    "django_tex",
    "infocurricular",
    "publications",
    "gallery",
    "research",
    "portafolio",
    "contact",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proyectoWeb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "physimathcode/plantillas",
            BASE_DIR / "cursos/plantillas",
            BASE_DIR / "fisicalab1/plantillas",
            BASE_DIR / "fisicalab2/plantillas",
            BASE_DIR / "autenticacion/plantillas",
            BASE_DIR / "classroom/plantillas",
            BASE_DIR / "infocurricular/plantillas",
            BASE_DIR / "publications/plantillas",
            BASE_DIR / "gallery/plantillas",
            BASE_DIR / "research/plantillas",
            BASE_DIR / "portafolio/plantillas",
            BASE_DIR / "contact/plantillas",
        ],
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
    {
        "APP_DIRS": True,
        "NAME": "tex",
        "BACKEND": "django_tex.engine.TeXEngine",
        "DIRS": [
            BASE_DIR / "fisicalab1/plantillas",
            BASE_DIR / "classroom/plantillas",
            # BASE_DIR / "infocurricular/plantillas",
            # BASE_DIR / "publications/plantillas",
            # BASE_DIR / "gallery/plantillas",
            # BASE_DIR / "research/plantillas",
            # BASE_DIR / "portafolio/plantillas",
            # BASE_DIR / "contact/plantillas",
        ],
    },
]

WSGI_APPLICATION = "proyectoWeb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "db_physimath_mysql",
    #     "USER": "root",
    #     "PASSWORD": "reT@urns20",
    #     "HOST": "localhost",
    #     "PORT": "3306",
    # }
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "media",
]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'


MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LATEX_GRAPHICSPATH = [
    os.path.join(
        settings.BASE_DIR,
        "static",
        "img",
        "fisilab1",
        "ajuste_de_curvas",
    ),
    os.path.join(
        settings.BASE_DIR,
        "static",
        "img",
        "classroom",
    ),
]

LATEX_INTERPRETER = "pdflatex"
X_FRAME_OPTIONS = "SAMEORIGIN"

XS_SHARING_ALLOWED_METHODS = ["POST", "GET", "OPTIONS", "PUT", "DELETE"]
