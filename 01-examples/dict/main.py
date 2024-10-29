"""
Eksempler på brugen af datastrukturen 'dict' (også kaldet en 'dictionary')
"""

# Eksempel 1 - Hvordan man skaber en 'dict'
person = {
    "name": "Jonas",
    "age": 41,
    "likes": ["Bad Omens", "The Prodigy", "Pink Floyd"],
}
dictator = dict(name="Guido", age=99, likes=["Python", "Being a Dictator"])


# Example 1.1 - Duplikater ikke tilladt (sidste 'key-value' par overskriver foregående)
car = {"brand": "Volvo", "speed": 250, "prod_year": 2000, "prod_year": 2012}
print(car)


# Eksempel 2 - Hvordan man tilgår en 'value' fra en 'key'
name = dictator["name"]
age = dictator.get("age")


# Eksempel 3 - Hvordan man får alle 'keys', 'values' eller begge dele fra 'dict'
person_keys = person.keys()
person_values = person.values()
person_keys_and_values = person.items()


# Eksempel 4 - Hvordan man ændrer og tilføjer en 'key-value' par i en 'dict'
car["speed"] = 900  # Ændrer 'speed'
car.update({"prod_year": 2022})  # Ændrer 'prod_year'

car["color"] = "Yellow"  # Tilføjer 'color'
car.update({"horse_power": 400})


# Eksempel 5 - Hvordan man looper gennem 'values', 'keys' eller begge dele i en 'dict'
for val in car.values():
    print(val)


for key in car.keys():
    print(key)


for key, value in car.items():
    print(key, value)
