# <Method1> (think by myself)
def sum_of_digits(n):
    num = str(2**n)
    num
    sum = 0
    for i in range(0,len(num)):
        sum += int(num[i])
    return sum


sum_of_digits(1000)