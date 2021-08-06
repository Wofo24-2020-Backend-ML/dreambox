from rest_framework import serializers
from .models import CSVData
from django.contrib.auth import get_user_model

User = get_user_model()


class CSVDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CSVData
        #fields = ['user', 'symbole', 'file', 'date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']
        fields = '__all__'
        #read_only_fields = ('file',)



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)



