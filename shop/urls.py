"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from . import  settings, views, utils

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name='home'),
	url(r'^add_to_cart/', views.add_to_cart, name='add_to_cart'),
    url(r'^cart/',views.view_cart, name='view_cart'),
    url(r'^account/sign_in/$', views.sign_in, name='sign_in'),
    url(r'^account/logout/$', views.logout, name='logout'),
    url(r'^account/profile/$', views.profile, name='profile'),
    url(r'^account/login/$', views.login, name='login'),
    url(r'^files$', utils.files, name='files')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)