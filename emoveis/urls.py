from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from emoveis.views import ( index, loginView, logoutView,
                           cadastrar_imobiliaria, forgetPassword, 
                           verificaToken, redefinirPassword, adicionarAnuncioView )

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginView, name='loginView'),
    path('login/esqueceu-senha/', forgetPassword, name='forgetPassword'),
    path('login/esqueceu-senha/token', verificaToken, name='verificaToken'),
    path('login/esqueceu-senha/token/redefinirPassword', redefinirPassword, name='redefinirPassword'),
    path('logout/', logoutView, name='logoutView'),
    path('adicionarAnuncioView/', adicionarAnuncioView, name='adicionarAnuncioView'),
    

    # path('esqueceu-a-senha/', forgetPassword, name='forgetPassword'),
    path('cadastrar_imobiliaria/', cadastrar_imobiliaria, name='cadastrar_imobiliaria'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)