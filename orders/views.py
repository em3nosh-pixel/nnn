from django.http import HttpResponse

def index(request):
    return HttpResponse("مرحباً بك في تطبيق الطلبات (Orders) 🧾")
