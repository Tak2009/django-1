from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    # message sample: https://learndjango.com/tutorials/django-signup-tutorial
    path('register', views.register, name="register"),
    path('about', TemplateView.as_view(template_name = "home/tech_list.html"), name="tech"),
]
