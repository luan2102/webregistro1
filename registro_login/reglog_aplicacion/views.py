from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    # Si el usuario ya está autenticado, redirigir a la página de bienvenida
    if request.user.is_authenticated:
        return redirect('bienvenido')  # Reemplaza 'bienvenido' con el nombre de tu URL para la página de bienvenida
    
    # Si el usuario no está autenticado, renderizar la página de inicio de sesión
    return render(request, 'reglog_aplicacion/login.html')

def login(request):
    if request.method == 'POST':
        # Lógica para el inicio de sesión (implementar aquí la autenticación)
        # Por ahora, simplemente redirigimos a la página de bienvenida si el usuario es válido
        # De lo contrario, se mostrará nuevamente la página de inicio de sesión con un mensaje de error
        return redirect('bienvenido') if request.user.is_authenticated else render(request, 'reglog_aplicacion/login.html')

    # Si es una solicitud GET, simplemente renderizar la página de inicio de sesión
    return render(request, 'reglog_aplicacion/login.html')

def registro(request):
    # Lógica para el registro
    return render(request, 'reglog_aplicacion/registro.html')

def bienvenido(request):
    # Lógica para la página de bienvenida
    return render(request, 'reglog_aplicacion/bienvenido.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')  # Reemplaza 'login' con el nombre de tu URL para la página de inicio de sesión
