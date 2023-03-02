#  1. find d(n)
def d(n):
    list = []
    for i in range(1, n):
        if n % i ==0:
            list.append(i)
    return sum(list)

# 2. find amicable numbers under 10000

list_s = [0]*10000
list_amicable = set()

i = 2
while i <10000:
    if list_s[i] ==0:
        num = d(i)
        if d(num) == i and num != i:
            list_s[num] = 1
            list_s[i] = 1
            list_amicable.add(i)
            list_amicable.add(num)
    i += 1

list_amicable
sum(list_amicable)





