from django.contrib import admin
from .models import TroopType, Location, MilitaryUnit, Platoon, Personnel

admin.site.register(TroopType)
admin.site.register(Location)
admin.site.register(MilitaryUnit)
admin.site.register(Platoon)
admin.site.register(Personnel)
