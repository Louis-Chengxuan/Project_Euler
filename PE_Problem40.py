# Qestion:
# An irrational decimal fraction is created by concatenating the positive integers:
#               0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# 1. list generator
def find_list(n):
    list_fraction = []
    # number generator
    for num in range(0, 1000000):
        num = str(num)
        for digit in range(0, len(num)):
            list_fraction.append(num[digit])
    return list_fraction[n]

# 2. find answer
i = 1
p = 1
while i <= 1000000:
    p = p * int(find_list(i))
    i = i * 10
print(p)

