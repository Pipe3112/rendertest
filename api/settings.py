from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# Seguridad
# ========================
SECRET_KEY = 'django-insecure-$3v*o%=2@omq(8g22o+9eejd=(rz3@-8$_hhzp%gu&(se6+ww1'
DEBUG = False

ALLOWED_HOSTS = [
    "rendertest-1p34.onrender.com",  # dominio en Render
    "localhost",
    "127.0.0.1",
]

# ========================
# Aplicaciones instaladas
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias
    'mycalendar',

    # Terceros
    'rest_framework',
    "corsheaders",
]

# ========================
# Middleware
# ========================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # 👈 necesario en Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'api.wsgi.application'

# ========================
# CORS
# ========================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",              # frontend en local
    "https://rendertest-1p34.onrender.com",  # dominio Render
]

# Mientras pruebas, puedes abrir todo (no recomendado en prod)
# CORS_ALLOW_ALL_ORIGINS = True

# ========================
# Base de datos
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ⚠️ Nota: en Render lo ideal es PostgreSQL con dj_database_url

# ========================
# Validación de contraseñas
# ========================
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

# ========================
# Internacionalización
# ========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ========================
# Archivos estáticos
# ========================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ========================
# Default PK
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
