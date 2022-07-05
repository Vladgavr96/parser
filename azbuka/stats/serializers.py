from rest_framework import serializers
from .models import Couch


class CouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Couch
        fields = "__all__"
