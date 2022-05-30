from django.urls import path
from Shopping import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('locales/', views.locales, name="Locales"),
    path('patioDeComidas/', views.patioComidas, name="PatioDeComidas"),
    path('cine/', views.cine, name="Cine"),
    path('promociones/', views.promociones, name="Promociones"),
    #path('registro/', views.registro, name="Registro"),
    path('formulario/', views.formulario, name="Formulario"),
    #path('busquedaUsuario/', views.busquedaUsuario, name="BusquedaUsuario"),
    #path('buscar/', views.buscar),
    path('leerSuscriptos', views.leerSuscriptos, name="LeerSuscriptos"),
    path('borrarSuscripto/<suscripto_nombre>', views.borrarSuscriptos, name="BorrarSuscripto"),
    path('editarSuscripto/<suscripto_nombre>', views.editarSuscriptos, name="EditarSuscripto"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name="Shopping/logout.html"), name="Logout"),
    path('editarUsuario', views.editarUsuario, name="EditarUsuario"),


   
]
