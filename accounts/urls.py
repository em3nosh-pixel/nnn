from django.urls import path
from . import views

urlpatterns = [
    # ✅ إنشاء حساب
    path('register/', views.register_view, name='register'),

    # ✅ تسجيل الدخول
    path('login/', views.login_view, name='login'),

    # ✅ تسجيل الخروج
    path('logout/', views.logout_view, name='logout'),

    # ✅ الملف الشخصي
    path('profile/', views.profile_view, name='profile'),
    path('complete-profile/', views.complete_profile_view, name='complete_profile'),

]
