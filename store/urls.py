from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store_home'),  # الصفحة الرئيسية
    path('products/', views.products_list, name='products_list'),  # قائمة المنتجات
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # تفاصيل المنتج
]
