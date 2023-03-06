'''
Question:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
'''

# when n == 8 or n ==9, it cant be prime. largest n is 7.
# 1. prime list generator
def prime_check(num):
    n_digit = 10 ** (num)
    list_check = [0] * n_digit
    list_prime = [2]
    value = 3
    while value <= n_digit:
        if list_check[value] == 0:
            if pandigital_check(value) == True:
                list_prime.append(value)
            i = value
            while i < n_digit:
                list_check[i] = 1
                i += value
        value += 2
    for i in range(len(list_prime) - 1 , -1, -1):
        if list_prime[i] < 10 ** (num - 1):
            list_prime.remove(list_prime[i])
    return list_prime
# 2. pandigital check
def pandigital_check(number):
    num = len(str(number))
    list_pandigital = [str(i) for i in range(1, num + 1)]
    digit = set(str(number))
    digit = list(digit)
    digit.sort()
    if list_pandigital == digit:
        return True
    else:
        return False

print(prime_check(7)[-1])

