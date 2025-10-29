from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
import os

# ✅ تحميل القيم من ملف البيئة .env
load_dotenv()

# ========================
# 📂 المسار الأساسي للمشروع
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# 🔐 المفتاح السري
# ========================
SECRET_KEY = 'django-insecure-8=4%8acy%&ms#)r7z4%qv+(qcy^pvje@429eps%0c73+bco-y@'

# ========================
# ⚙️ وضع التطوير
# ========================
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


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


# ========================
# ☁️ إعدادات Cloudinary
# ========================
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# ========================
# الإعداد الافتراضي للمفاتيح
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
