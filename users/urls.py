from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.views import perfilView

urlpatterns = [
    path('<str:nome_usuario>/', perfilView, name='perfilView'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)