from django.contrib import admin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

@admin.register(Passengerinfo)
class PassengerinfoAdmin(LeafletGeoAdmin):
    list_display = ('passLocation', 'passDestination')


@admin.register(Depotstage)
class DepotstageAdmin(LeafletGeoAdmin):
    list_display = ('depotname', 'depotLocation')


@admin.register(Matatuinfo)
class MatatuinfoAdmin(LeafletGeoAdmin):
    list_display = ('plate', 'voyage', 'capacity', 'departureTime')


@admin.register(RouteDestinations)
class RouteDestinationsAdmin(LeafletGeoAdmin):
    list_display = ('to_PlaceName', 'from_PlaceName', 'Price', )

@admin.register(Driverinfo)
class DriverinfoAdmin(admin.ModelAdmin):
    list_display = ('driverName', 'driverVehicle')

@admin.register(Roads)
class RoadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'rtenme','geom')

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('location', 'destination', 'distance')

