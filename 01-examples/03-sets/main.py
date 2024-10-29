"""
Eksempler på brugen af 'set' datastrukturen
Examples of set data structure
"""

# Eksempel 1 - hvordan man skaber et "set"
fruits = {"apples", "bananas", "pears", "grapes", "strawberries"}
bands = set(["The Beatles", "The Rolling Stones", "Gasolin"])


# Eksempel 2 - hvordan man looper igennem et "set"
for fruit in fruits:
    print(fruit)


# Eksempel 3 - set metoder

bands.add("The Who")  # Tilføj med 'add'

bands.update({"Pink Floyd", "Queen"})  # Opdatere set med andet set

print(bands.intersection({"Aqua", "The Beatles", "Korn"}))  # Find fælles elementer
