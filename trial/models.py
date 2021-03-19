from django.db import models
from django.contrib.gis.db import models


# Create your models here.

class Roads(models.Model):
    id = models.IntegerField(primary_key=True)
    osm_id = models.FloatField(null=True)
    sourceid = models.CharField(max_length=254, null=True)
    notes = models.CharField(max_length=254, null=True)
    onme = models.CharField(max_length=254, null=True)
    rtenme = models.CharField(max_length=254, null=True)
    ntlclass = models.CharField(max_length=254, null=True)
    fclass = models.IntegerField(null=True)
    numlanes = models.IntegerField(null=True)
    srftpe = models.CharField(max_length=254, null=True)
    srfcond = models.CharField(max_length=254, null=True)
    isseasonal = models.CharField(max_length=254, null=True)
    curntprac = models.CharField(max_length=254, null=True)
    gnralspeed = models.IntegerField(null=True)
    rdwidthm = models.IntegerField(null=True)
    status = models.CharField(max_length=254, null=True)
    iselevated = models.IntegerField(null=True)
    iso3 = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    last_updat = models.CharField(max_length=254, null=True)
    geom = models.MultiLineStringField(srid=4326)


    class Meta:
        verbose_name_plural = 'Roads'

    def __str__(self):
        return str(self.rtenme)


class Depotstage(models.Model):
    depotname = models.CharField(null=True, max_length=150)
    depotLocation = models.PointField(null=True)
    mat_in = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Depotstage'

    def __str__(self):
        return self.depotname


class RouteDestinations(models.Model):
    objects = None
    from_PlaceName = models.CharField(max_length=100, null=True)
    from_Place = models.PointField(null=True)
    to_PlaceName = models.CharField(max_length=100, null=True)
    to_Place = models.PointField(null=True)
    Price = models.IntegerField(null=True)
    boardDepot = models.ForeignKey(Depotstage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'To {self.to_PlaceName} From {self.from_PlaceName} '

    class Meta:
        verbose_name_plural = 'RouteDestinations'
        ordering = ['to_PlaceName']


class Matatuinfo(models.Model):
    objects = None
    plate = models.CharField(max_length=8, null=True)
    capacity = models.IntegerField(null=True)
    FullOccupancy = models.BooleanField(default=False)
    voyage = models.ForeignKey(RouteDestinations, on_delete=models.CASCADE, null=True)
    currentLocation = models.PointField(null=True)
    departureTime = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'MatatuInfo'

    def __str__(self):
        return self.plate


class Passengerinfo(models.Model):
    passDestination = models.PointField(null=True)
    passLocation = models.PointField(null=True)

    class Meta:
        verbose_name_plural = 'Passengerinfo'

    def __str__(self):
        return str(self.passLocation)

class Driverinfo(models.Model):
    driverName = models.CharField(null=True, max_length=250)
    driverVehicle = models.ForeignKey(Matatuinfo, on_delete=models.CASCADE, null=True)
    driverSchedule = models.ForeignKey(RouteDestinations, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Driverinfo"
        ordering = ['driverName']

    def __str__(self):
        return self.driverName

class Measurement(models.Model):
    location = models.CharField(max_length=200, null=True)
    destination = models.CharField(max_length=200, null=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Distance form (self.location) to (self.destination) is (self.distance)km"