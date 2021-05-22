from django.db.models import fields
from rest_framework import serializers
from .models import *

class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ["beacon_local", "beacon_espaco"]

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalApp
        fields = ["beacon_local", "nome", "telefone", "texto"]