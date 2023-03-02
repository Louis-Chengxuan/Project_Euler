# 1. prime
def primes(n):
    flag = True
    if n == 2:
        return True
    if n == 1 or n ==0:
        return False
    for i in range(2,n):
        if n % i ==0:
            flag = False
    if flag == True:
        return True

# 1.find all primes list 
list_prime = [2]
list = [0]*1000000
value = 3
count = 1
while value < 1000000:
    if list[value] == 0:
        count +=1
        list_prime.append(value)
        i = value
        while i < 1000000:
            list[i] = 1
            i += value
    value += 2
len(list_prime)

list_prime

# 2. narrow down
list_circular = []
for i in range(0,78498):
    num = str(list_prime[i])
    for d in range(0,len(num)):
        if int(num) % 3 ==0 or int(num[d])==0 or int(num[d]) == 2 or int(num[d]) ==4 or int(num[d]) ==5 or int(num[d])==6 or int(num[d]) ==8:
            break
        elif d == len(num)-1:
            list_circular.append(num)

len(list_circular)
list_circular


list_potential = list_circular

# 3. find_code 

list_code = []
for i in range(0,len(list_potential)):
    n = list_potential[i]
    f_d = 0
    s_d = 0
    t_d = 0
    fr_d = 0
    for d in range(0,len(n)):
        if int(n[d]) == 1:
            f_d += 1
        elif int(n[d]) == 3:
            s_d += 1
        elif int(n[d]) == 7:
            t_d += 1
        elif int(n[d]) == 9:
            fr_d += 1
    list_code.append(str(f_d) + str(s_d) + str(t_d) + str(fr_d))

len(list_code)

# 4. n! funx
def xx(n):
    p = 1 
    for i in range(2,n+1):
        p = p * i
    return p


# 5. code choice function

def test(code):
    count = 0
    choice = 1
    # catch the code
    for d in range(0,4):
        v = int(code[d])
        if v != 0:
            count += v
    for d in range(0,4):
        v = int(code[d])
        if v != 0:
            choice = choice * (xx(count) / xx(count-v) / xx(v))
            count += -v
    return int(choice)

# 6. final: count code
list_finalround = []
for i in range(0,1110):
    code = list_code[i]
    if test(code) == 1:
        list_finalround.append(1)
    elif test(code) == list_code.count(code):
        list_finalround.append(test(code))


sum(list_finalround)

#(2,3,5)
answer = sum(list_finalround) + 3 
print(answer)