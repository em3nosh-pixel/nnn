from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # ✅ إنشاء حساب
    path('register/', views.register_view, name='register'),

    # ✅ تسجيل الدخول
    path('login/', views.login_view, name='login'),

    # ✅ تسجيل الخروج
    path('logout/', LogoutView.as_view(next_page='store_home'), name='logout'),

    path('profile/', views.profile_view, name='profile'),

]
