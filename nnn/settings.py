from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ✅ تحميل ملف البيئة أولاً
load_dotenv()

# ✅ إعدادات Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

# ========================
# 📂 المسار الأساسي للمشروع
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# 🔐 المفتاح السري
# ========================
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')

# ========================
# ⚙️ وضع التطوير
# ========================
DEBUG = False  # ✅ لإتاحة عمل الموقع على الإنترنت
ALLOWED_HOSTS = ['*']  # ✅ السماح لكل النطاقات (Render)

# ========================
# 🧩 التطبيقات المثبتة
# ========================
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project Apps
    'accounts',
    'store',
    'orders',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ========================
# ⚙️ الوسائط الوسيطة
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ WhiteNoise لتقديم الملفات الثابتة بعد النشر
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# 🌐 نظام التوجيه
# ========================
ROOT_URLCONF = 'nnn.urls'

# ========================
# 🎨 إعدادات القوالب
# ========================
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

# ========================
# 🚀 إعدادات WSGI
# ========================
WSGI_APPLICATION = 'nnn.wsgi.application'


# ========================
# 💾 قاعدة البيانات
# ✅ استخدام SQLite محلياً
# ✅ وعلى Render يستخدم PostgreSQL تلقائياً باستخدام DATABASE_URL
# ========================
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
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
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ========================
# 🖼️ الملفات الثابتة
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ تفعيل WhiteNoise للملفات الثابتة
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ========================
# ☁️ إعدادات Cloudinary
# ========================
STORAGES = {
    'default': {
        'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
    },
}

# ========================
# 📦 إعدادات Media
# ========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========================
# الإعداد الافتراضي للمفاتيح
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
