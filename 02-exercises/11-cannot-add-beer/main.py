"""
I nedenstående ser du en indkøbliste, som din kone har lavet.

Du vil imidlertid VIRKELIG gerne tilføje flere øl til denne liste.

Lav derfor et program, hvor en bruger kan tilføje 3 flere varer til listen, hvoraf én af indtastninger SKAL være 'øl'.

Når dette er gjort skal dit program udskrive den nye liste i pænt format via et loop.
"""

shopping_list = {"mælk", "øl", "brød"}

for _ in range(3):
    item = input("Hvad vil du tilføje? ")
    shopping_list.add(item)


print("\nINDKØBSLISTE")
for item in shopping_list:
    print(f"- {item}")
