from rest_framework import serializers
from todo.models import Task, Tile
from rest_framework import exceptions
from django.contrib.auth import authenticate


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'order_number', 'description', 'task_type', 'tile', 'owner', 'created_at')


class TileSerializer(serializers.ModelSerializer):
    task_set = TaskSerializer(many=True, read_only=True)
        
    class Meta:
        model = Tile
        fields = ('id', 'launch_date', 'status', 'task_set', 'owner', 'created_at')
 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password =data.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to log in with the provided credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide both username and password"
            raise exceptions.ValidationError(msg)
        return data
