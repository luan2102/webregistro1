from django.contrib import admin
from django.urls import path
from reglog_aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    # URL raíz, redirige a la página de inicio de sesión si el usuario no está autenticado,
    # de lo contrario, redirige a la página de bienvenida
    path('', views.index),
]
