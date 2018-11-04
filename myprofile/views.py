from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from myprofile.forms import ProfileForm, UserForm
from myprofile.models import Profile, User

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
            messages.success(request, 'Your profile has been created')
            return redirect('index')
        else:
            messages.error(request, user_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def update_profile():
    pass


def delete_profile(request):
    u = User.objects.get(pk=request.user.pk)
    u.delete()
    messages.success(request, 'Profile deleted')
    return redirect('index')


def login_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'User logged in')
                return redirect('index')
            else:
                messages.warning(request, 'Account is disabled')
        else:
            messages.error(request, 'Invalid Login')
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def logout_profile(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('index')


def perm_profile():
    pass


def change_password():
    pass


def reset_password():
    pass
