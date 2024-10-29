list1 = ["M", "na", "i", "Jo"]
list2 = ["y", "me", "s", "nas"]

sentence = ""

for i in range(len(list1)):
    sentence += list1[i] + list2[i] + " "

print(sentence)
