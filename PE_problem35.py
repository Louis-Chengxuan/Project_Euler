# 1. find prime list
list = [0]*1000000
list_prime = []
value = 3
while value < 1000000:
    if list[value] ==0:
        list_prime.append(str(value))
        i = value
        while i < 1000000:
            list[i] = 1
            i += value
    value += 2

list_prime
new_prime = []

# 2. narrow down
for i in range(0,len(list_prime)):
    num = list_prime[i]
    for d in range(0,len(num)):
        if int(num[d]) % 2 ==0:
            break
        elif d == len(num) -1:
            new_prime.append(num)

new_prime
len(new_prime)

# 2. find circular prime list:
count = 1
list_circular = ["2"]
for i in range(0,3217):
    n = str(new_prime[i])
    if len(n) == 1:
        count += 1
        list_circular.append(n)
    else:
        new_n = n
        for d in range(0,len(n)-1):
            new_n = new_n[1:len(n)] + new_n[0]
            if new_n not in new_prime:
                break
            elif d == len(n) - 2:
                count += 1
                list_circular.append(n)

len(list_circular)
list_circular

count

