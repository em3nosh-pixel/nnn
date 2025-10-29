from django.urls import path
from . import views

urlpatterns = [
    # ✅ الصفحة الرئيسية
    path('', views.home, name='store_home'),

    # ✅ قائمة المنتجات
    path('products/', views.products_list, name='products_list'),

    # ✅ تفاصيل المنتج
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
]
