
def Count_Chain(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num + 1
        count += 1
    return count

def longest_Chain(limit_num):
    max_num = 0
    max_Count = 0
    for num in range(1,limit_num):
        if Count_Chain(num) > max_Count:
            max_Count = Count_Chain(num)
            max_num = num
    return max_num

longest_Chain(1000000)

