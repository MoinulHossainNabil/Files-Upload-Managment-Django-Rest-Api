from rest_framework import serializers

from .models import FileModel


class FileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'
