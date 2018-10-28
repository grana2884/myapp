from django.shortcuts import render
from myprofile.forms import ProfileForm, UserForm


def index(request):
    return render(request, 'home.html')


def create_profile(request):
    registered = False

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
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered':
        registered})


def update_profile():
    pass


def delete_profile():
    pass


def login_profile():
    pass


def logout_profile():
    pass


def perm_profile():
    pass


def change_password():
    pass


def reset_password():
    pass
