import phonenumbers
from phonenumbers import geocoder, carrier

# Enter your number with country code and ddd #
phoneNumer = phonenumbers.parse("+55xxxxxxxxxxx") # -> enter a number here.

# capture provider #
carrier = carrier.name_for_number(phoneNumer, 'pt-br')

# capture region #
region = geocoder.description_for_number(phoneNumer, 'pt-br')

# Mostra resultados #
print(f"PROVIDER: {carrier}.")
print(f"STATE UF: {region}.")