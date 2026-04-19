"""
URL configuration for Projeto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls.base import reverse_lazy
from Playlists import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Playlists.urls')),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', LoginView.as_view(template_name='seguranca/login.html'), name='login'),
    path('meu-logout/', views.logout_usuario, name='meu-logout'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('homepage')), name='logout'),
    path(
        'seguranca/password_change/', 
        PasswordChangeView.as_view(
            template_name='seguranca/password_change_form.html',
            success_url=reverse_lazy('sec-password_change_done'),
        ),
        name='sec-password_change'
    ),
    path(
        'seguranca/password_change_done/',
        PasswordChangeDoneView.as_view(
            template_name='seguranca/password_change_done.html',
        ),
        name='sec-password_change_done'
    ),
]

