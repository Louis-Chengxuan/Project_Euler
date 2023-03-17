'''
Q:The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

# 1. find prime list
marked = [0] * 10000
list_prime = []
value = 3

while value < 10000:
    if marked[value] == 0:
        i = value
        if value > 1000 and value < 9999:
            list_prime.append(value)
        while i < 10000:
            marked[i] = 1
            i += value
    value += 2

# 2. find prime value with same digits
list_same_prime = []
for i in list_prime:
    set_num = set(str(i))
    if set_num not in list_same_prime:
        list_same_prime.append(set_num)
print(list_same_prime)



# 3. find same value prime in the list
list_all = []
for i in list_same_prime:
    list_three = []
    for j in list_prime:
        number = set(str(j))
        if number == i:
            list_three.append(j)
    if len(list_three) >= 3:
        list_all.append(list_three)

# 4. compare each list in list_all
from itertools import combinations

for i in list_all:
    for a, b in combinations(i, 2):
        c = (a + b) // 2
        if c in i:
            print(a, b, c)

        


