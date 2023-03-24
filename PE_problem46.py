'''Q:
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2 x 1**2
15 = 7 + 2 x 2**2
21 = 3 + 2 x 3**2
25 = 7 + 2 x 3**2
27 = 19 + 2x 2**2
33 = 31 + 2 x 1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''

# 1. create a prime list
def prime_list(n):
    marked = [0] * n
    list_prime = [2]
    value = 3
    while value < n:
        if marked[value] == 0:
            list_prime.append(value)
            i = value
            while i < n:
                marked[i] = 1
                i += value
        value += 2 
    return list_prime

# 2. odd check function
def is_odd_composite(n):
    n = str(n)
    flag = True
    for i in str(n):
        if int(i) % 2 == 0:
            flag = False
    if flag:
        return True
    else:
        return False 
    
# 3. final check function, check the question
def elements_less_than_num(input_list, num):
    return [element for element in input_list if element < num]


def is_integer(value):
    if isinstance(value, int):
        return True
    elif isinstance(value, float):
        return value.is_integer()
    else:
        return False

# Usage examples:
print(is_integer(5))  # Output: True
print(is_integer(5.0))  # Output: True
print(is_integer(3.2))  # Output: False
print(is_integer("hello"))  # Output: False


# 4. find the smallest odd composite.
for i in range(50, 10000):
    if is_odd_composite(i) and i not in prime_list(10000):
        list_p = elements_less_than_num(prime_list(10000), i)
        flag = False
        for j in list_p:
            num = ((i - j) // 2) ** 0.5
            if is_integer(num) == True:
                flag = True
        if flag == False:
            print(i, j, num)

