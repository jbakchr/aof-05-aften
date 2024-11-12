"""
Recap fra 4. aften om operatorer
"""

# Eksempel 1 - Om 'aritmetiske' operatorer
x = 20
y = 3

addition = x + y  # 23
subtraction = x - y  # 17
multiplication = x * y  # 60
division = x / y  # 6.666666666666667
modulus = x % y  # 2
floor_division = x // y  # 6


# Eksempel 2 - Om 'tildelingsoperatorer' operatorer
x = 1000
y = 500

x += y  # x = 1500
x -= y  # x = 1000
x *= y  # x = 500000

running_total = 0

for i in range(1, 5):
    running_total += i  # 1 + 2 + 3 + 4 = 10


# Eksempel 3 - Om 'sammenligningsoperatorer'
x = 10
y = 20

is_equal = x == y  # False
is_not_equal = x != y  # True
is_greater_than = x > y  # False
is_less_than = x < y  # True


# Eksempel 4 - Om 'logiske operatorer'
x = 10
y = 20
z = 30

and_operator = x < y and y > z  # False
or_operator = x < y or y > z  # True
not_operator = not x < y  # False

is_started = False

while not is_started:
    print("Starting...")
    is_started = True
