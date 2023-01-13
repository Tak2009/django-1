from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views


app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    # message sample: https://learndjango.com/tutorials/django-signup-tutorial
    path('register', views.register, name="register"),
]
