from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    # https://ordinarycoders.com/blog/article/django-user-register-login-logout
    path('register', views.register_request, name="register"),
]
