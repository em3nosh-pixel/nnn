from pathlib import Path
import os

# ========================
# 📂 المسار الأساسي للمشروع
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# 🔐 المفتاح السري (SECRET KEY)
# ⚠️ لا تشارك هذا المفتاح خارج بيئة التطوير
# ========================
SECRET_KEY = 'django-insecure-8=4%8acy%&ms#)r7z4%qv+(qcy^pvje@429eps%0c73+bco-y@'


# ========================
# ⚙️ وضع التطوير (DEBUG)
# ========================
DEBUG = True
ALLOWED_HOSTS = []


# ========================
# 🧩 التطبيقات المثبتة (INSTALLED_APPS)
# ========================
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع الخاصة
    'accounts',
    'store',
    'orders',
]


# ========================
# ⚙️ الوسائط الوسيطة (Middlewares)
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ← لدعم الترجمة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================
# 🌐 نظام التوجيه (URLs)
# ========================
ROOT_URLCONF = 'nnn.urls'


# ========================
# 🎨 إعدادات القوالب (Templates)
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← مسار القوالب الرئيسي
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


# ========================
# 🚀 إعدادات WSGI
# ========================
WSGI_APPLICATION = 'nnn.wsgi.application'


# ========================
# 💾 قاعدة البيانات (SQLite)
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ========================
# 🔐 التحقق من كلمات المرور
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ========================
# 🌍 اللغة والمنطقة الزمنية
# ========================
LANGUAGE_CODE = 'ar'              # ← اللغة العربية
TIME_ZONE = 'Asia/Riyadh'         # ← المنطقة الزمنية للسعودية
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ========================
# 🖼️ الملفات الثابتة (Static Files)
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # ← ملفات المشروع أثناء التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'    # ← مجلد تجميع الملفات عند النشر


# ========================
# 📦 الملفات الإعلامية (Media Files)
# ========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ========================
# ⚙️ الإعداد الافتراضي للمفاتيح
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

