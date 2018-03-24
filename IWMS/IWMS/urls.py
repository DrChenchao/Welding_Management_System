"""IWMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from User_Information.views import *


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^edit_staff/$', edit_staff, name='edit_staff'),
    url(r'', include('INDEX.urls', namespace='INDEX')),
	url(r'^Project_Management/', include('Project_Management.urls', namespace='Project_Management')),
    url(r'^Staff_Management/', include('Staff_Management.urls', namespace='Staff_Management')),
    url(r'^WPS_Management/', include('WPS_Management.urls', namespace='WPS_Management')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^Material_Management/',include('Material_Management.urls', namespace='Material_Management')),
    url(r'^User_Information/', include('User_Information.urls', namespace='User_Information')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
