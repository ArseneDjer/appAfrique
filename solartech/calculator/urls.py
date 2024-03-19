from django.urls import path
from .views import SolarSystemCreateView

urlpatterns = [
    path('calculate/', SolarSystemCreateView.as_view(), name='calculate_solar_system'),
]