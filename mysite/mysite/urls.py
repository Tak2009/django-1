"""samples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.views.generic import TemplateView
from daisy.apis import LoginView, LogoutView

urlpatterns = [
    # path('', include('ads.urls')),
    path('', include('home.urls')),
    path('onestop/', include('onestop.urls')),
    path('daisy/', include('daisy.urls')),
    path('api/v1/', include('daisy.api_urls')),
    # path('api/v1/auth/', include('rest_framework.urls')), # https://youtu.be/ekhUhignYTU?list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&t=863
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),
    path('plant/', include('plant.urls')),
    path('admin/', admin.site.urls),
    # https://learndjango.com/tutorials/django-login-and-logout-tutorial
    # https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.views
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^apps/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, '../'),
         'show_indexes': True},
        name='index_path'
        ),
]

# Serve the favicon -
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')

# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include
