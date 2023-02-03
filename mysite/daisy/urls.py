from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name='daisy'
urlpatterns = [
    path('', views.PicListView.as_view(), name='all'),
    path('pic/<int:pk>', views.PicDetailView.as_view(), name='pic_detail'),
    path('pic/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='pic_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(), name='pic_comment_delete'),
]