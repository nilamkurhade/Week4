"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from myapp import views
from rest_framework.authtoken import views as rest_framework_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('myapp/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    url('Registration/', views.RegistrationList.as_view()),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)