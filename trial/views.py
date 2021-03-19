from django.shortcuts import render, get_object_or_404

from routetrial import settings
from .models import *
from django.views.generic import ListView
from django.db.models import Q
from.forms import *
from geopy.geocoders import Nominatim
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
from geopy.distance import geodesic
import folium


# Create your views here.


def homepage(request):
    return render(request, "trial/homepage.html")


def passengerpage(request):
    availablematatu = Matatuinfo.objects.all
    getprice = RouteDestinations.objects.all
    context = {'availablematatu': availablematatu,
               'getprice': getprice
               }
    return render(request, 'trial/passenger.html', context)


def passenger2page(request):
    return render(request, 'trial/trial2.html')

def passenger3page(request):
    return render(request, 'trial/kelly.index.html')

class SearchDestinationView(ListView):
    model = Matatuinfo
    template_name = 'trial/kelly.index.html'

    def get_queryset(self):
        query1 = self.request.GET.get('q1')
        query2 = self.request.GET.get('q2')
        object_list = Matatuinfo.objects.filter(
            Q(name__icontains=query1) | Q(name__icontains=query2)
        )
        return object_list


def passenger5page(request):
    return render(request, 'trial/kelly.services.html')


def Passenger4page(request,):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent="trial")

    ip_ = get_ip_address(request)
    print(ip_)
    ip = '41.89.240.109'
    country, city, lat, lon = get_geo(ip)
    #print('location country', country)
    #print('location city', city)
    #print('location lat, lon', lat, lon)

    location = geolocator.geocode(city)

    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # folium map
    m = folium.Map(width=320, height=250, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)

    folium.Marker(
        [l_lat, l_lon], popup=city['city'], tooltip='click here for more', icon=folium.Icon(color='purple')
    ).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        print(destination)
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat, d_lon)

        distance = round(geodesic(pointA,pointB).km, 2)
        # folium map

        m = folium.Map(width=320, height=250, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon),
                       zoom_start=get_zoom(distance))
        # location marker
        folium.Marker(
            [l_lat, l_lon], popup=city['city'], tooltip='click here for more', icon=folium.Icon(color='purple')
        ).add_to(m)
        # destination marker
        folium.Marker(
            [d_lat, d_lon], popup=destination, tooltip='click here for more',
            icon=folium.Icon(color='blue', icon='cloud')).add_to(m)

        # draw line between points
        line = folium.PolyLine(locations=[pointA, pointB], weight=1, color='black')
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()

    m = m._repr_html_()

    context = {
        'distance': obj,
        'form': form,
        'map': m,
    }
    return render(request, 'trial/kelly.about.html', context)
