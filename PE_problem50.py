'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

# 1. create prime_list
def prime_list(num):
    marked = [0] * num
    value = 3
    list_prime = [2]

    while value < num:
        if marked[value] == 0:
            list_prime.append(value)
            i = value
            while i < num:
                marked[i] = 1
                i += value
        value += 2
    
    return list_prime 

# 2. assume it is 
import time
start_time = time.time()

list_prime = prime_list(1000000)
prime_set = set(list_prime)
max_cnt = 0

max_prime = 0
for i in range(0, len(list_prime) - 1):
    sum_prime = 0
    n = i
    cnt = 0
    while sum_prime < 1000000:
        sum_prime += list_prime[n]
        n += 1
        cnt += 1
        if sum_prime in prime_set and cnt > max_cnt:
            max_prime = sum_prime
            max_cnt = cnt
print(max_prime, max_cnt)

end_time = time.time()
elapsed_time = end_time - start_time
print('the code took', elapsed_time, 'seconds to execute.')


