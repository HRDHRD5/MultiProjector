"""
URL configuration for multiprojector project.

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
import os
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import redirect
from multiprojector import views

def redirect_static(request, match):
    host = os.getenv("static-host-redirect")
    host = host[:-1] if host[-1] == "/" else host
    return redirect(f"{host}{request.path}")

urlpatterns = [
    path("streaming-api/", include("streaming.urls")),
    re_path(r"^.*$", views.index, name="frontend"),
]

if os.getenv("static-host-redirect") is not None and os.getenv("static-host-redirect") != "":
    urlpatterns.insert(-2, re_path(
        rf"^(src|node_modules/).*$", redirect_static))

if os.getenv("admin-page-enabled") is not None and os.getenv("admin-page-enabled").lower() == "true":
    urlpatterns.insert(-2, path('admin/', admin.site.urls))