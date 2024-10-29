keys = ["Ti", "Tyve", "Tredive"]
values = [10, 20, 30]

res = {}

for i in range(len(keys)):
    res.update({keys[i]: values[i]})

print(res)
