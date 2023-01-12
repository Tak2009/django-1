from django.urls import path
from django.views.generic import TemplateView

app_name='daisy'
urlpatterns = [
    path('', TemplateView.as_view(template_name="daisy_list.html"), name='all'),
]