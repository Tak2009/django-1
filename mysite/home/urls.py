from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    path('register', views.register, name="register"), # message sample: https://learndjango.com/tutorials/django-signup-tutorial
    path('about', views.TechView.as_view(), name="tech"), # django async with token version: https://youtu.be/28KFBqi2JrA?t=900 
    # path('about', TemplateView.as_view(template_name = "home/tech_list.html"), name="tech"), # javascript async with no token version
]


