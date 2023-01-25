
from django.urls import path, include
from daisy.apis import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('', PicViewSet)

# urlpatterns = [
#     path('pics/', include(router.urls))
# ]

# exe pics func in apis.py
urlpatterns = [
    ### class APIView based ###
    path('pics/', PicAPIView.as_view()),
    path('pics/<int:id>/', PicDetailAPIView.as_view()),
    ### function based ###
    # path('pics/', pics),
    # path('pics/<int:id>/', pic_detail),

]