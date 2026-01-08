from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret")

DEBUG = True

ALLOWED_HOSTS = ["*"]

# -----------------------------
# Applications
# -----------------------------
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

# -----------------------------
# Database
# -----------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "core.urls"

# -----------------------------
# Templates
# -----------------------------
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

# -----------------------------
# Static Files (CRITICAL)
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------
# Django REST
# -----------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# -----------------------------
# JAZZMIN CONFIG (THIS IS THE UI)
# -----------------------------
JAZZMIN_SETTINGS = {
    "site_title": "Healthcare Admin",
    "site_header": "Healthcare Management System",
    "site_brand": "WhatByte",
    "welcome_sign": "Welcome back 👋",

    "navigation_expanded": True,

    "hide_apps": ["auth"],
    "hide_models": ["auth.Group"],

    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"name": "GitHub", "url": "https://github.com/harsh164", "new_window": True},
    ],

    "icons": {
        "accounts.User": "fas fa-user-circle",
        "doctors.Doctor": "fas fa-user-md",
        "patients.Patient": "fas fa-hospital-user",
        "patients.PatientDoctor": "fas fa-notes-medical",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    "show_sidebar": True,

    "theme": "darkly",  # 🔥 IMPORTANT
}
