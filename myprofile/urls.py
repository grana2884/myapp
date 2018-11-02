from django.urls import path
from myprofile import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.create_profile, name='register'),
    path('login/', views.login_profile, name='login'),
    path('change_password/', views.change_password, name='change_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
