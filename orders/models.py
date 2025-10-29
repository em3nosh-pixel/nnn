from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', _("قيد التنفيذ")),
        ('completed', _("مكتمل")),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("المستخدم"))
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)
    status = models.CharField(_("الحالة"), max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = _("الطلب")
        verbose_name_plural = _("الطلبات")

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_("الطلب"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("المنتج"))
    quantity = models.PositiveIntegerField(_("الكمية"), default=1)
    price = models.DecimalField(_("السعر"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _("عنصر الطلب")
        verbose_name_plural = _("عناصر الطلب")

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
