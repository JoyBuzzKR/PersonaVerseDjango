# myapp/serializers.py

from rest_framework import serializers

class MyBeanieDocumentSerializer(serializers.Serializer):
    """
    Beanie Document를 표현하기 위한 DRF Serializer
    """
    id = serializers.CharField(read_only=True)  # MongoDB _id -> str로 변환해서 전달
    title = serializers.CharField(required=True, max_length=200)
    description = serializers.CharField(required=False, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)