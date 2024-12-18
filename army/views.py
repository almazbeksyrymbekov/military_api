from rest_framework.viewsets import ModelViewSet
from .models import TroopType, Location, MilitaryUnit, Platoon, Personnel
from .serializers import TroopTypeSerializer, LocationSerializer, \
MilitaryUnitSerializer, PlatoonSerializer, PersonnelSerializer

class TroopTypeViewSet(ModelViewSet):
    queryset = TroopType.objects.all()
    serializer_class = TroopTypeSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MilitaryUnitViewSet(ModelViewSet):
    queryset = MilitaryUnit.objects.all()
    serializer_class = MilitaryUnitSerializer


class PlatoonViewSet(ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer


class PersonnelViewSet(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer