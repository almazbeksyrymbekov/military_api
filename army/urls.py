from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TroopTypeViewSet, LocationViewSet,MilitaryUnitViewSet, PlatoonViewSet, PersonnelViewSet

router = DefaultRouter()
router.register(r'troop-types', TroopTypeViewSet, basename='trooptype')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'military-units', MilitaryUnitViewSet, basename='militaryunit')
router.register(r'platoons', PlatoonViewSet, basename='platoon')
router.register(r'personnel', PersonnelViewSet, basename='personnel')



urlpatterns = [
] + router.urls
