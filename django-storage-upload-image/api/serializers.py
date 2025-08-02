from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "description", "image", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]
