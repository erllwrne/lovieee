from pathlib import Path
import os

# --------------------------
# BASE
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# SECURITY
# --------------------------
SECRET_KEY = 'your-secret-key-here'  # replace with a real secret key
DEBUG = True  # Set False in production
ALLOWED_HOSTS = ["*"]  # or ["lovieee-uis2.onrender.com"] for production

# --------------------------
# INSTALLED APPS
# --------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',  # your app
]

# --------------------------
# MIDDLEWARE
# --------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# URLS & WSGI
# --------------------------
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

# --------------------------
# DATABASE (default SQLite)
# --------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------
# TEMPLATES
# --------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# --------------------------
# PASSWORD VALIDATION
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------
# INTERNATIONALIZATION
# --------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_TZ = True

# --------------------------
# STATIC FILES (CSS, JS, etc.)
# --------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # where collectstatic puts files
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # local static files folder
]

# --------------------------
# MEDIA FILES (uploaded images)
# --------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------
# DEFAULT AUTO FIELD
# --------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
