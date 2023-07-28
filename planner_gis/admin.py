from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Myplaces



@admin.register(Myplaces)
class MyplacesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location',)
