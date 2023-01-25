from rest_framework import viewsets, routers
from daisy.models import Pic
from daisy.serializers import PicSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# class PicViewSet(viewsets.ModelViewSet):
#     queryset = Pic.objects.all()
#     serializer_class = PicSerializer

### class APIView based ###
class PicAPIView(APIView):
    def get(self, request):
        pictures =Pic.objects.all()
        serialized = PicSerializer(pictures, many=True)
        return Response(serialized.data, status=200)

    def post(self, request):
        data = request.data
        serialized = PicSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class PicDetailAPIView(APIView):
    def get_object(sefl, id):
        try:
            return Pic.objects.get(id=id)
        except Pic.DoesNotExist as e:
            raise Http404
    
    def get(self, request, id=None):
        instance = self.get_object(id)
        serialized = PicSerializer(instance)
        return Response(serialized.data)
    
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serialized = PicSerializer(instance, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

### function based ###
# @csrf_exempt # required for post
# def pics(request):
#     if request.method == 'GET':
#         pictures =Pic.objects.all()
#         serialized = PicSerializer(pictures, many=True)
#         return JsonResponse(serialized.data, safe=False)
#     elif request.method == "POST":
#         json_parser = JSONParser()
#         data = json_parser.parse(request)
#         serialized = PicSerializer(data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return JsonResponse(serialized.data, status=201)
#         return JsonResponse(serialized.errors, status=400)

# @csrf_exempt # required for put, delete
# def pic_detail(request, id):
#     try:
#         instance = Pic.objects.get(id=id)
#     except Pic.DoesNotExist as e:
#         return JsonResponse( {"error": "Pic object not found."}, status=404)
    
#     if request.method == 'GET':
#         serialized = PicSerializer(instance)
#         return JsonResponse(serialized.data, safe=True)
#     elif request.method == "PUT":
#         json_parser = JSONParser()
#         data = json_parser.parse(request)
#         serialized = PicSerializer(instance, data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return JsonResponse(serialized.data, status=200)
#         return JsonResponse(serialized.errors, status=400)
#     elif request.method == 'DELETE':
#         instance.delete()
#         return HttpResponse(status=204)