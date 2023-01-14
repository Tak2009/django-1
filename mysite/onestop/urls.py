from django.urls import path, reverse_lazy
from . import views

app_name='onestop'
urlpatterns = [
    path('', views.RecipeListView.as_view(), name='all'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create',
        views.RecipeCreateView.as_view(success_url=reverse_lazy('onestop:all')), name='recipe_create'),
    path('recipe/<int:pk>/update',
        views.RecipeUpdateView.as_view(success_url=reverse_lazy('onestop:all')), name='recipe_update'),
    path('recipe/<int:pk>/delete',
        views.RecipeDeleteView.as_view(success_url=reverse_lazy('onestop:all')), name='recipe_delete'),
    path('recipe_picture/<int:pk>', views.stream_file, name='recipe_picture'),
    path('recipe/<int:pk>/note',
        views.NoteCreateView.as_view(), name='recipe_note_create'),
    path('note/<int:pk>/delete',
        views.NoteDeleteView.as_view(), name='recipe_note_delete'),
    path('recipe/<int:pk>/favorite', views.AddFavoView.as_view(), name='recipe_favorite'),
    path('recipe/<int:pk>/unfavorite', views.DeleteFavoView.as_view(), name='recipe_unfavorite'),
    path('recipe/tags', views.TagListView.as_view(), name='tag_list'),
]

#Use reverse_lazy in urls.py to delay looking up the view until all the paths are defined