from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ✅ إنشاء حساب جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠ اسم المستخدم موجود مسبقًا")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "✅ تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول")
        return redirect("login")

    return render(request, "accounts_t/register.html")



# ✅ تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "✅ تم تسجيل الدخول بنجاح")
            return redirect("store_home")
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة")
            return redirect("login")

    return render(request, "accounts_t/login.html")



# ✅ صفحة لوحة المستخدم (اختياري - سنستخدمها لاحقًا)
@login_required(login_url='login')
def profile_view(request):
    return render(request, "accounts_t/profile.html")
