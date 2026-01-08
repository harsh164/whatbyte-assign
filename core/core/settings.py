from pathlib import Path
from dotenv import load_dotenv
import os
from datetime import timedelta
import dj_database_url

# --------------------------------------------------
# Base setup
# --------------------------------------------------
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")
DEBUG = True

ALLOWED_HOSTS = ["*"]

# --------------------------------------------------
# Applications
# --------------------------------------------------
INSTALLED_APPS = [
    "jazzmin",  # MUST be first

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "accounts",
    "patients",
    "doctors",
]

AUTH_USER_MODEL = "accounts.User"

# --------------------------------------------------
# Database (Render PostgreSQL)
# --------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}

# --------------------------------------------------
# Django REST Framework + JWT
# --------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# --------------------------------------------------
# Middleware
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# --------------------------------------------------
# URLs & Templates
# --------------------------------------------------
ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
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

WSGI_APPLICATION = "core.wsgi.application"

# --------------------------------------------------
# Internationalization
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Static files (THIS IS THE KEY FIX)
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# JAZZMIN CONFIG (UI / UX)
# --------------------------------------------------
JAZZMIN_SETTINGS = {
    # Branding
    "site_title": "Healthcare Admin",
    "site_header": "Healthcare Management System",
    "site_brand": "WhatByte",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Welcome back 👋",

    # Layout
    "navigation_expanded": True,
    "show_sidebar": True,

    # Hide default auth clutter
    "hide_apps": ["auth"],
    "hide_models": ["auth.Group"],

    # Top Menu
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {
            "name": "GitHub",
            "url": "https://github.com/harsh164",
            "new_window": True,
        },
    ],

    # Icons
    "icons": {
        "accounts.User": "fas fa-user-circle",
        "doctors.Doctor": "fas fa-user-md",
        "patients.Patient": "fas fa-hospital-user",
        "patients.PatientDoctor": "fas fa-notes-medical",
    },

    # Forms UI
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "accounts.user": "collapsible",
    },
}
