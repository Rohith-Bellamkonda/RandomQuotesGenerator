from rest_framework import serializers
from .models import *


class SerializerModelQuote(serializers.ModelSerializer):
    class Meta:
        model = ModelQuote
        fields = '__all__'