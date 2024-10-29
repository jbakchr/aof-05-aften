accoutance = ("revenue", [5000, 7000, 6000], "costs", [4500, 5000, 3000])

revenue = accoutance[1]
costs = accoutance[3]

profit = 0

for i in range(len(revenue)):
    profit += revenue[i] - costs[i]

print(profit)
