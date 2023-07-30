from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Stop


@admin.register(Stop)
class StopAdmin(LeafletGeoAdmin):
    list_display = (
        "name",
        "location",
    )
