from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'base.html', {'form': form})


def salir(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/')
def inicio(request):
    user = request.user
    return render(request, 'inicio.html', {'usuario':user})

def registroUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registroUser.html', {'form': form})