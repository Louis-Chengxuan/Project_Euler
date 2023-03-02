
def Fibonacci(num):
    a, b = 1, 1
    c = a + b
    index = 3
    while len(str(c)) < num:
        index += 1
        a = b
        b = c 
        c = a + b
    return index 

Fibonacci(1000)