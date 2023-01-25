
from django.urls import path, include
from daisy.apis import *
from rest_framework import routers

# ### class ModelViewSet based ###
router = routers.DefaultRouter()
router.register('pics', PicViewSet)

pic_list_view = PicViewSet.as_view({
    "get":"list",
    "post": "create"
})

urlpatterns = [
    # ### class ModelViewSet based ###
    path('pics/', include(router.urls)),

    # ### class GenericAPIView based ###
    # path('generic/pics/', pic_list_view), # this is equal to: path('generic/pics/', PicListView.as_view())
    # path('generic/pics/', PicListView.as_view()),
    # path('generic/pics/<int:id>/', PicListView.as_view()),

    # ### class APIView based (comment out class ModelViewSet based first to test here and vice versa)###
    # path('pics/', PicAPIView.as_view()),
    # path('pics/<int:id>/', PicDetailAPIView.as_view()),
    # ### function based ### exe pics and pic_detail funcs in daisy.apis.py

    # path('pics/', pics),
    # path('pics/<int:id>/', pic_detail),

]