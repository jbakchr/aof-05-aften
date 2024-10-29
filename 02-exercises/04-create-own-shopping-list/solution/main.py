shopping_list = []

for _ in range(3):
    item = input("Indtast en vare til du vil tilføje tilshoppinglisten: ")
    shopping_list.append(item)

print("Din shoppingliste:")
for item in shopping_list:
    print(f"- {item}")
