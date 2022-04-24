from .models import PRG
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField ,TaggitSerializer)


class PRGSerializer(TaggitSerializer,serializers.ModelSerializer):
    image = serializers.ImageField(required= False)
    tags = TagListSerializerField()
    # slug = serializers.SlugField(required=False)

    class Meta:
        model = PRG
        fields = '__all__'
