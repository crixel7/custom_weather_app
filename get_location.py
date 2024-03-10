import geopy
import folium

def get_location(address):
    geolocator = geopy.Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    return location

print(get_location("Bristol, UK"))