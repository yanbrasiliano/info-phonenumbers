import phonenumbers
from phonenumbers import geocoder, carrier
"""

Created by: Yan Brasiliano Silva Penalva
Objective: View phone operator and number state.

"""

print()
print('Author: Yan Brasiliano Silva Penalva - hiyan')
print()

# Enter your number with country code and ddd #
phoneNumer = phonenumbers.parse("+55xxxxxxxxxxx") # -> enter a number here.

# capture provider #
carrier = carrier.name_for_number(phoneNumer, 'pt-br')

# capture region #
region = geocoder.description_for_number(phoneNumer, 'pt-br')

# Mostra resultados #
print(f"PROVIDER: {carrier}.")
print(f"STATE UF: {region}.")