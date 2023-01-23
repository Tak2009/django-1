from rest_framework import viewsets, routers
from daisy.models import Pic
from daisy.serializers import PicSerializer
 
class PicViewSet(viewsets.ModelViewSet):
    queryset = Pic.objects.all()
    serializer_class = PicSerializer
 
router = routers.DefaultRouter()
router.register(r'pics', PicViewSet)