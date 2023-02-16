
from daisy.models import Pic
from daisy.serializers import PicSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework import viewsets, routers, status, generics, mixins
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django.core.exceptions import PermissionDenied

# ### class ModelViewSet ###
class PicViewSet(viewsets.ModelViewSet):
    serializer_class = PicSerializer
    queryset = Pic.objects.all()
    lookup_field = 'id'
    # https://youtu.be/ekhUhignYTU?list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&t=863
    # https://testdriven.io/blog/drf-views-part-1/
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    # https://testdriven.io/blog/drf-views-part-3/
    @action(detail=True, methods=['POST'])
    def upload(self, request):
        serializer = PicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return Response(serializer.data)

    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user != obj.created_by: 
            raise PermissionDenied('You are not allowed to  modify listing')
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user != obj.created_by: 
            raise PermissionDenied('You are not allowed to delete')
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)


### class GenericAPIView ###
class PicListView(generics.GenericAPIView, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    ):
    serializer_class = PicSerializer
    queryset = Pic.objects.all()
    lookup_field = 'id'
    # https://youtu.be/ekhUhignYTU?list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&t=863
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
    # def post(self, request):
    #     return self.create(request)

    # # overriding the one defined in CreateModelMixin
    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

    # def put(self, request, id=None):
    #     return self.update(request, id)

    # # overriding the one defined in UpdateModelMixin
    # def perform_update(self, serializer):
    #     serializer.save(created_by=self.request.user)
    
    # def delete(self, request, id=None):
    #     return self.destroy(request, id)

### class APIView based ###
# class PicAPIView(APIView):
#     def get(self, request):
#         pictures =Pic.objects.all()
#         serialized = PicSerializer(pictures, many=True)
#         return Response(serialized.data)

#     def post(self, request):
#         data = request.data
#         serialized = PicSerializer(data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# class PicDetailAPIView(APIView):
#     def get_object(sefl, id):
#         try:
#             return Pic.objects.get(id=id)
#         except Pic.DoesNotExist as e:
#             raise Http404
    
#     def get(self, request, id=None):
#         instance = self.get_object(id)
#         serialized = PicSerializer(instance)
#         return Response(serialized.data)
    
#     def put(self, request, id=None):
#         data = request.data
#         instance = self.get_object(id)
#         serialized = PicSerializer(instance, data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None):
#         instance = self.get_object(id)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ### function based ###
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


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)