# 1. Method1: mathmatic method

# 1, check is_pentagonal?
import math

def is_pentagonal(n):
    if (math.sqrt(n * 24 + 1) + 1) % 6 == 0:
        return True
    return False

# 2. find D
flag = True
y = 2
is_pentagonal()
while flag:
    for x in range(1, y):
        a = x * (3 * x - 1) / 2
        b = y * (3 * y - 1) / 2
        if is_pentagonal(a + b) and is_pentagonal(b - a):
            flag = False
            print(b - a)
            break
    y += 1


# Method2 in PE forum: using itertools (combination)
import itertools

pentagonals = {int(n*(3*n-1)/2) for n in range(1,2900)}

for j,k in itertools.combinations(pentagonals,2):
  if k-j not in pentagonals or j+k not in pentagonals: 
     continue
  print(k-j)
  break

# my method
p = []
for i in range(1, 3000):
    p.append(i*(3*i -1 )/2)

for i in range(1,3000):
    for j in range(i+1, 2999):
        if (p[i] + p[j] in p) and (p[j] - p[i] in p):
            D = p[j] - p[i]
            print(p[i] , p[j] , D)