from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Bienvenido a la API del calendario 🚀",
        "endpoints": {"admin": "/admin/", "api": "/api/"}
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("mycalendar.urls")),
]
