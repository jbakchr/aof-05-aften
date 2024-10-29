import random

primes_until_fifty = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

random_numbers = set()

for i in range(10):
    random_numbers.add(random.randint(1, 50))

print(random_numbers.intersection(primes_until_fifty))
