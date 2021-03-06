"""testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from erp.admin import erp_admin # broken
from django.urls import path, include#, url
import debug_toolbar
from .settings import use_grappelli

urlpatterns = [
    path('admin/', admin.site.urls),
    path('UI/', include ('UI.urls')),
    path('erp/', erp_admin.urls),
    path('chaining/', include('smart_selects.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    #url(r'^chaining/', include('smart_selects.urls')),
    #path(r'_nested_admin/', include('nested_admin.urls')),
    #url(r'^_nested_admin/', include('nested_admin.urls')),
]
if use_grappelli:
    urlpatterns.insert(0, path('grappelli/', include('grappelli.urls'))) # grappelli URLS grp
