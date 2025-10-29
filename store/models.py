from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("اسم الفئة"), max_length=100, unique=True)
    description = models.TextField(_("الوصف"), blank=True, null=True)

    class Meta:
        verbose_name = _("الفئة")
        verbose_name_plural = _("الفئات")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name=_("الفئة"))
    name = models.CharField(_("اسم المنتج"), max_length=150)
    description = models.TextField(_("الوصف"), blank=True, null=True)
    price = models.DecimalField(_("السعر"), max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(_("المخزون"), default=0)
    image = models.ImageField(_("صورة المنتج"), upload_to="products/", blank=True, null=True)  # ✅ جديد
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("المنتج")
        verbose_name_plural = _("المنتجات")

    def __str__(self):
        return self.name
