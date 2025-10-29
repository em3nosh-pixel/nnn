from django.shortcuts import render, get_object_or_404
from .models import Product


# ✅ الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')


# ✅ عرض جميع المنتجات
def products_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, "store_t/products_list.html", {"products": products})


# ✅ صفحة تفاصيل المنتج
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store_t/product_detail.html", {"product": product})
