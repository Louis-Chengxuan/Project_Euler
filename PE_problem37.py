#1. find all primes
list = [0]*1000000
list_primes = ['2']
value = 3 
while value <= 1000000:
    if list[value] == 0:
        i = value
        list_primes.append(str(value))
        while i < 1000000:
            list[i] = 1
            i += value
    value += 2 


# 2. narrow down
def narrow_down(num):
    for i in range(0,len(str(num))):
        if int(str(num)[i]) in [4,6,8]:
            return False
        elif int(str(num)[i]) not in [4,6,8]  and i == len(str(num))-1:
            return True
        
list_narrow_primes = []
for i in range(0,len(list_primes)):
    num = int(list_primes[i])
    if narrow_down(num):
        list_narrow_primes.append(str(num))

list_narrow_primes
list_primes = list_narrow_primes

#3. find truncatable primes
list_trun = []
count = 0
i = -1
while count <11:
    i += 1
    num = str(list_primes[i])
    n,m = num, num
    for x in range(1,len(num)):
        if num not in list_primes:
            break
        n = n[1:len(n)]
        m = m[0:len(m)-1]
        if n not in list_primes or m not in list_primes:
            break
        elif n in list_primes and m in list_primes and x == len(num)-1:
            list_trun.append(int(num))
            count += 1

sum(list_trun) 