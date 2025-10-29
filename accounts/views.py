from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ✅ إنشاء حساب جديد + توجيه لصفحة إكمال البيانات
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠ اسم المستخدم موجود مسبقًا")
            return redirect("register")

        # ✅ إنشاء المستخدم
        user = User.objects.create_user(username=username, password=password)

        # ✅ تسجيل دخول مباشر بعد إنشاء الحساب
        login(request, user)

        # ✅ الانتقال لصفحة إدخال الجوال والعنوان
        return redirect("complete_profile")

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



# ✅ إكمال بيانات المستخدم
@login_required(login_url='login')
def complete_profile_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        # ✅ حفظ البيانات داخل Profile
        request.user.profile.phone = phone
        request.user.profile.address = address
        request.user.profile.save()

        messages.success(request, "✅ تم حفظ البيانات بنجاح ✅")

        # ✅ نقل المستخدم للصفحة الرئيسية
        return redirect("store_home")

    return render(request, "accounts_t/complete_profile.html")



# ✅ صفحة البروفايل
@login_required(login_url='login')
def profile_view(request):
    return render(request, "accounts_t/profile.html")



# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.success(request, "✅ تم تسجيل الخروج بنجاح")
    return redirect("store_home")
