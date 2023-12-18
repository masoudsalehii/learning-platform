from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created. Please login.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"{field.capitalize()}: {error}")
            return redirect('register')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('all-todos')
        else:
            messages.warning(request, 'something went wrong.')
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out. Please login')
    return redirect('login')


