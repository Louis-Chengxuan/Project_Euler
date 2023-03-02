count = 0
for c_200 in range(0,2):
    for c_100 in range(0,(200-200*c_200)//100+1):
        for c_50 in range(0,(200-200*c_200-100*c_100)//50 + 1):
            for c_20 in range(0,(200-200*c_200-100*c_100-50*c_50)//20 + 1):
                for c_10 in range(0,(200-200*c_200-100*c_100-50*c_50-20*c_20)//10 + 1):
                    for c_5 in range(0,(200-200*c_200-100*c_100-50*c_50-20*c_20 - 10*c_10)//5 + 1):
                        for c_2 in range(0,(200-200*c_200-100*c_100-50*c_50-20*c_20-10*c_10-5*c_5)//2 + 1):
                            count += 1

count


# new_method
num_list = [2,5,10,20,50,100,200]
def find_list():
    list= []
    for num in num_list:
        for i in range(1,200//num+1):
            list.append(num*i)
    list.sort()
    return list

find_list()

for i in range(0,100):

sum = 200
coins = [1,2,5,10,20,50,100,200]

table = [0 for k in range(200+1)]
table[0] = 1

for i in range(0,len(coins)):
    for j in range(coins[i],sum+1):
        table[j]+= table[j-coins[i]]
        
print(table[sum])
table[sum]

table = [0 for k in range(200+1)]


coins = [1, 2, 5]

def count(money, max_coin = 5):
    cnt = 0
    if money == 0 or money == 1:
        return 1 
    for coin in coins:
        if coin > max_coin or coin > money:
            break
        cnt += count(money - coin, coin)
    return cnt

print(count(5))
count(9,1) + count(8,2) + count(5,5)


