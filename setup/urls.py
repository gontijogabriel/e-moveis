from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emoveis.urls')),
    path('perfil/', include('users.urls')),
]
