from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("المستخدم"))
    phone = models.CharField(_("رقم الجوال"), max_length=20, blank=True, null=True)
    address = models.CharField(_("العنوان"), max_length=255, blank=True, null=True)
    joined_at = models.DateTimeField(_("تاريخ الانضمام"), auto_now_add=True)

    class Meta:
        verbose_name = _("الملف الشخصي")
        verbose_name_plural = _("الملفات الشخصية")

    def __str__(self):
        return f"{self.user.username}"
