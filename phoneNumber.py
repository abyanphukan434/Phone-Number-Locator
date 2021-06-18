import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

Key = '6c88f3edf15448a582a99183d722b39c'

number = "+91 9435033886"

myNumber = phonenumbers.parse(number)

myLocation = geocoder.description_for_number(myNumber, "en")

print(myLocation)

service_number = phonenumbers.parse(number, "AS")

print(carrier.name_for_number(service_number, "en"))

geocoder = OpenCageGeocode(Key)

query = str(myLocation)

results = geocoder.geocode(query)

print(results)

lat = results[0]["geometry"]["lat"]

lng = results[0]["geometry"]["lng"]

print(lat, lng)

myMap = folium.Map(location = [lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = myLocation).add_to(myMap)

myMap.save("myLocation.html")