
list = []

for x in range(2,10**6):
    sum = 0
    for digit in str(x):
        sum += int(digit)**5
    if sum == x:
        list.append(sum)


sum = 0
for i in range(0,len(list)):
    sum += list[i]
print(sum)
