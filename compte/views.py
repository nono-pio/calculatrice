from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from compte.forms import CreateUserForm

def register_view(request):
    context = {}
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compte')

    context['form'] = form
    return render(request,'compte/register.html', context=context)

def login_view(request):
    context = {
        'data': {}
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('compte')
        else:
            context['data']['error_login'] = True

    return render(request, 'compte/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')

def compte_view(request):
    user = request.user
    if not user.is_authenticated :
        return redirect('login')
    context = {} 
    return render(request,'compte/compte.html', context=context)