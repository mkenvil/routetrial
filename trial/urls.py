from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('passenger', views.passengerpage, name='passenger_page'),
    path('passenger2/', views.passenger2page, name='passenger2'),
    path('passenger3/', views.passenger3page, name='passenger3'),
    path('passenger4/', views.Passenger4page, name='passenger4'),
    path('passenger5/', views.passenger5page, name='passenger5'),


]