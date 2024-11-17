from rest_framework import serializers

from attachments.models import FileAttachments, AudioAttachments
from attachments.Utils.formatter import Formatter

from django.conf import settings

class FileAttachmentsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FileAttachments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['size'] = Formatter.format_bytes(instance.size)
        data['src'] = f"{settings.CURRENT_URL}{instance.src}"

        return data
    

class AudioAttachmentsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AudioAttachments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['src'] = f"{settings.CURRENT_URL}{instance.src}"

        return data