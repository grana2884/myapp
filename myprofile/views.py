from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from myprofile.forms import ProfileForm, UserForm


def index(request):
    return render(request, 'home.html')


def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def update_profile():
    pass


def delete_profile():
    pass


def login_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
        else:
            print("Invalid Login")
            return redirect('index')
    else:
        return render(request, 'login.html', {})


def logout_profile(request):
    logout(request)
    return redirect('index')


def perm_profile():
    pass


def change_password():
    pass


def reset_password():
    pass
