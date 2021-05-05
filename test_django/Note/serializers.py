from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    author = serializers.CharField()

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance