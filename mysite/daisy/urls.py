from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name='daisy'
urlpatterns = [
    path('', views.PicListView.as_view(), name='all'),
]