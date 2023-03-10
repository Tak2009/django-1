from rest_framework import serializers
from daisy.models import Pic
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# HyperlinkedModelSerializer: https://youtu.be/ruIJdGdgkCw?list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&t=1313
# class PicSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pic
#         # fields ='__all__'
#         fields = ('id','title', 'pic', 'url')


class PicSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    
    class Meta:
        model = Pic
        fields = ('id','title', 'pic', 'created_by')
        read_only_fields = ('created_by', )
    
    # https://stackoverflow.com/questions/56056449/how-to-get-username-of-users-post-in-django-rest-api-instead-of-number
    # check SerializerMethodField and django.contrib.auth.models.User
    def get_created_by(self, obj):
        # print(type(obj.created_by))
        return {
            "id": obj.created_by.id,
            "first_name": obj.created_by.first_name,
            "last_name": obj.created_by.last_name
        }


# https://www.youtube.com/watch?v=g8Sz2mF0ENU&list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&index=8
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
