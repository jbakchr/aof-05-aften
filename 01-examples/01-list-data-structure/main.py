"""
Eksempler på brugen af 'list' datastrukturen
"""

# Eksempel 1 - Hvordan man skaber en 'list' via "bracket notation" og "list" funktionen
my_list = ["apple", "banana", "beer", "chips", "coca cola"]
my_second_list = list(("apple", "banana", "beer"))


# Eksempel 2 - Hvordan man tilgår elementer i en liste
first_element = my_list[0]
last_element = my_list[-1]
beer_and_chips = my_list[2:4]
dont_buy_coca_cola = my_list[:4]


# Eksempel 3 - Hvordan man tjekker en liste for et element
if "beer" in my_list:
    print("Beer is awesome!")


# Example 4 - Hvordan man ændrer et element i en liste
my_list[4] = "wine"


# Example 5 - Hvordan man bruger metoder på lister
my_list.append("oranges")
my_list.insert(1, "cheese")


# Eksempel 6 - Hvordan man looper over et liste
for el in my_list:
    print(el)
