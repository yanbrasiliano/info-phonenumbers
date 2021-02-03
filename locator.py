import phonenumbers
from phonenumbers import geocoder, carrier

# Enter your number with country code and ddd #
phoneNumer = phonenumbers.parse("+5551999999999")

# capture provider #
Carrier = carrier.name_for_number(phoneNumer, 'pt-br')

# capture region #
Region = geocoder.description_for_number(phoneNumer, 'pt-br')

# Mostra resultados #
print(f"PROVIDER: {carrier}.")
print(f"STATE UF: {Region}.")