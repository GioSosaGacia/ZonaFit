import phonenumbers
from phonenumbers import geocoder,timezone,carrier
#https://www.geeksforgeeks.org/phonenumbers-module-in-python/

phone_number1 = phonenumbers.parse('+523334653335')
print('\n Phone number location\n')
print(geocoder.description_for_number(phone_number1,'esp'));

timeZone = timezone.time_zones_for_number(phone_number1)
print(phone_number1)
print(timeZone)

Carrier = carrier.name_for_number(phone_number1, 'esp')
Region = geocoder.description_for_number(phone_number1, 'en')
print(Carrier)
print(Region)


#checar esta info tambien para localizar un numero mobil
#https://c43s4rs.blogspot.com/2018/02/scripts-de-geolocalizacion-en-python.html
