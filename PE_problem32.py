


count = 0
list_p = set()
for a in range(1,100):
    for b in range(1,10000):
        list = []
        if len(str(a)) + len(str(b)) + len(str(a*b)) != 9 or a*b > 9999 or a*b < 1000:
            count += 0
        else:
            num = str(a) + str(b) + str(a*b)
            for i in range(0,len(num)):
                list.append(num[i])
            list.sort()
            if list == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                list_p.add(a*b)
                count += 1
                print(a,b,a*b)


list_p 
sum(list_p)