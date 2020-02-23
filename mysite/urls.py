"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('nested_admin/', include('nested_admin.urls')),
    path('robots.txt', lambda request: redirect('/static/blog/robots.txt', permanent=True)),
    path('favicon.ico', lambda request: redirect('/static/blog/Logo.ico', permanent=True)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:home'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login-account'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='blog:home'), name='logout-account'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
]
