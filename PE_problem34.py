# 1. find area
i = 1
num = 0
num1 = 1
while int(num) < num1:
    num = "9"* i
    num1 = 362880 * i
    i += 1

# max len i is 7
# max num is 2177280)

int('9'* 2)
num1

# 2. def scan function
def scan(digit):
    p = 1
    for i in range(2,digit+1):
        p = p * i
    return p


# 3. num
list = []
for num in range(3,2540160):
    sum = 0 
    if num in [7,8,9] and num >= 5040: 
        for digit in range(0,len(str(num))):
            sum += scan(int(str(num)[digit]))
        if sum == num:
            list.append(sum)
    elif num not in [7,8,9] and num <5040:
        for digit in range(0,len(str(num))):
            sum += scan(int(str(num)[digit]))
        if sum == num:
            list.append(sum)


list

if 9 in list:
    print(1)

# <new method>

def new_scan(n):
    if n == 9:
        return 362880
    if n == 8:
        return 40320
    if n == 7:
        return 5040
    if n == 6:
        return 720
    if n ==5:
        return 120
    if n ==4:
        return 24
    if n ==3:
        return 6
    if n ==2:
        return 2
