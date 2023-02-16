from django.urls import path, include
from todo.apis import *
from rest_framework import routers

# ### class ModelViewSet based ###
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tiles', TileViewSet)


urlpatterns = [
    # ### class ModelViewSet based ###
    path('todo/', include(router.urls)),
]