from django.urls import path
from django.views.generic import TemplateView

app_name='plant'
urlpatterns = [
    path('', TemplateView.as_view(template_name="plant_list.html"), name='all'),
]