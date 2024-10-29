"""
Eksempler på brugen af 'tuple' datastrukturen
"""

# Eksempel 1 - Hvordan man skaber en "tuple"
my_tuple = ("apple", "banana", "beer", "pears", "chips", "cheese")

tuple_from_iterable = tuple(["Jonas", 41, True, ["cheese", "cake", 42]])

tuple_with_one_element = ("WTF",)


# Eksempel 2 - Hvordan man får længden og typen af en tuple
print(f"Length of 'my_tuple': {len(my_tuple)}")
print(type(my_tuple))


# Eksempel 3 - Hvordan man tilgår elementer i en tuple med "bracket notation"
print(f"Second element is: {my_tuple[1]}")
print(f"Second last element: {my_tuple[-2]}")
print(f"First two elements are: {my_tuple[0:2]}")


# Eksempel 4 - Hvordan man tjekker for et element i en tuple
if "beer" in my_tuple:
    print("Beer is awesome!")


# Eksempel 5 - Hvordan man opdaterer en tuple (selvom originalen egentlig ikke kan ændres ..)
change_tuple = ("apple", "pears", "beers")  # Original tuple
change_to_list = list(change_tuple)  # Ændre tuple til list
change_to_list[0] = "cheese"  # Ændre elementer
change_tuple = tuple(change_to_list)  # Ændre opdateret list til tuple igen


# Eksempel 6 - "Unpack" en tuple
groceries = ("beer", "bananas", "pears", "ost")

beer, *other_stuff = groceries
print(f"{beer} is the best ..")
print(f"And the rest are: {other_stuff}")
