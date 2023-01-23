from rest_framework import serializers
from daisy.models import Pic

class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = ['title', 'picture', 'created_at']