from todo.models import Task, Tile
from todo.serializers import TaskSerializer, TileSerializer, LoginSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser
from django.core.exceptions import PermissionDenied


# ### class ModelViewSet ###
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (JSONParser, MultiPartParser)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(serializer.data)

    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user != obj.owner: 
            raise PermissionDenied('You are not allowed to  modify listing')
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user != obj.owner: 
            raise PermissionDenied('You are not allowed to delete')
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)


# ### class ModelViewSet ###
class TileViewSet(viewsets.ModelViewSet):
    serializer_class = TileSerializer
    queryset = Tile.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (JSONParser, MultiPartParser)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return Response(serializer.data)

    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user != obj.owner: 
            raise PermissionDenied('You are not allowed to modify')
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user != obj.owner: 
            raise PermissionDenied('You are not allowed to delete')
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginTodoView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id}, status=200)


class LogoutTodoView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)



# Reference 
# https://ilovedjango.com/django/rest-api-framework/views/tips/sub/modelviewset-django-rest-framework/
# https://stackoverflow.com/questions/55081085/validate-user-on-update-request-in-django-rest-framework
# https://stackoverflow.com/questions/46053922/delete-method-on-django-rest-framework-modelviewset