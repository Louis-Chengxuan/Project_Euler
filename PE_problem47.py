'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?'''

def prime_factors(num):
    factors = set()
    # divide by 2 until it's odd
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    # check odd numbers up to the square root of num
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    # if num is a prime greater than 2, it is a prime factors, add it to the set of factors
    if num > 2:
        factors.add(num)
    return factors 
#(by using this algorithm)

cnt = 0
num = 2 * 3 * 4 * 5 # smallest number that has 4 distinct prime factors

while cnt < 4:
    num += 1
    if len(prime_factors(num)) == 4:
        cnt += 1
    else:
        cnt = 0
print(num - 3)
