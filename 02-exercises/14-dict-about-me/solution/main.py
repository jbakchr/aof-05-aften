me = {"name": "", "age": 0, "hobbies": []}

me["name"] = input("Navn: ")
me["age"] = int(input("Alder: "))

for i in range(3):
    hobby = input("Hobby: ")
    me["hobbies"].append(hobby)

print(me)
