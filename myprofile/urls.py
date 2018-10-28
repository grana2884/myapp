from django.urls import path
from myprofile import views

urlpatterns = [
    path('', views.index, name='index'),
    path()
]
