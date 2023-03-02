def factorial(num):
    p = 1
    for i in range(1,num+1):
        p = p * i
    return p


factorial(10)

def sum_of_digits(num):
    list = str(factorial(num))
    sum = 0
    for i in range(0,len(str(factorial(num)))):
        sum += int(list[i])
    return sum

sum_of_digits(100)