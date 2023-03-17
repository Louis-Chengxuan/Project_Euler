'''
QUESTION:
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''
# 1. def x ** x function.

def x_Powerx(num):
    return num ** num


# 2. find sum
sum = 0
for i in range(1, 1001):
    num = str(x_Powerx(i))
    sum += int(num[-10:])
sum = str(sum)[-10:]

print(sum)








