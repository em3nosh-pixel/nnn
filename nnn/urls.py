from django.contrib import admin
from django.urls import path, include
from store import views  # ✅ مهم جداً

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # صفحة تواصل معنا
    path('contact/', views.contact, name='contact'),

    # المتجر + الصفحة الرئيسية
    path('', include('store.urls')),

    # حسابات المستخدمين
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]
