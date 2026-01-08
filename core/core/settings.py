from pathlib import Path
from dotenv import load_dotenv
import os
from datetime import timedelta
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "jazzmin", 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'accounts',
    'patients',
    'doctors',
]

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # --------------------
    # Branding
    # --------------------
    "site_title": "Healthcare Admin",
    "site_header": "Healthcare Management System",
    "site_brand": "WhatByte",
    "welcome_sign": "Welcome back 👋",

    # --------------------
    # Layout
    # --------------------
    "navigation_expanded": True,
    "hide_apps": ["auth"],
    "hide_models": ["auth.Group"],

    # --------------------
    # Top Menu
    # --------------------
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"name": "GitHub", "url": "https://github.com/harsh164", "new_window": True},
    ],

    # --------------------
    # Icons (IMPORTANT)
    # --------------------
    "icons": {
        "accounts.User": "fas fa-user-circle",
        "doctors.Doctor": "fas fa-user-md",
        "patients.Patient": "fas fa-hospital-user",
        "patients.PatientDoctor": "fas fa-notes-medical",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    # --------------------
    # UI Tweaks
    # --------------------
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "accounts.user": "collapsible",
    },

    "show_sidebar": True,
}

