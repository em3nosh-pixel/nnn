from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ✅ لوحة تحكم المدير
    path('admin/', admin.site.urls),

    # ✅ روابط التطبيقات
    path('accounts/', include('accounts.urls')),  # مستخدمين
    path('store/', include('store.urls')),        # المتجر
    path('orders/', include('orders.urls')),      # الطلبات

    # ✅ الصفحة الرئيسية توجّه تلقائيًا للمتجر
    path('', include('store.urls')),
]

# ✅ إعدادات عرض الملفات أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

