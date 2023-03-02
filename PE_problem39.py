def p(num):
    count = 0
    for a in range(1,int(num/2) ):
        for b in range(1,a):
            c = num / 2 - (a*b) / num
            if a + b + c == num and c >=0 and c == int(c):
                count += 1
    return count

count_new = 0
for i in range(3,1001):
    if p(i) >= count_new:
        count_new = p(i)
        max_i = i
print(max_i)



