from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

class LoginView(View):

    def get(self, request):
        return render(
            request,
            'home/login.html',
        )

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')

# Realiza una acción según si el usuario se encuentra logeado.
@login_required(login_url='login')
# Diseña la vista del sitio principal.
def index_view(request):
    return render(
        # Corre el html que diseña la vista principal.
        request,
        'home/index.html',
    )