from rest_framework import serializers
from .models import TroopType, Location, MilitaryUnit, Platoon, Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'

class PlatoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platoon
        fields = '__all__'

class MilitaryUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryUnit
        fields = '__all__'

class TroopTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TroopType
        fields = '__all__'  


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'  
