#  Copyright (c) 2019.
#  Ahmad Syafiq Kamil

from . import views
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('',views.login, name='login'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.Profile.as_view(), name='profil'),


]