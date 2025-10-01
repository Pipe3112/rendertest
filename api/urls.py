from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Vista de prueba para la raíz
def home(request):
    return JsonResponse({
        "message": "Bienvenido a la API del calendario 🚀",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/"
        }
    })

urlpatterns = [
    path('', home),  # 👈 evita el error 400 en Render
    path('admin/', admin.site.urls),
    path('api/', include('mycalendar.urls')),  # 👈 ahora tu API está en /api/
]
