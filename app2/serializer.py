from rest_framework import serializers

from app2.models import Topic



class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'     