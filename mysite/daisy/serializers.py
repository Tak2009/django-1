from rest_framework import serializers
from daisy.models import Pic

# HyperlinkedModelSerializer: https://youtu.be/ruIJdGdgkCw?list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&t=1313
# class PicSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pic
#         # fields ='__all__'
#         fields = ('id','title', 'pic', 'url')

class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = ('id','title', 'pic')