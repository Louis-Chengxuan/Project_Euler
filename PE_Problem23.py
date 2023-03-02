
def abundant_num(num):
    s = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            s += i
            if i != num // i:
                s += num//i
    if s>num:
        return True

abundant_list = set()
for i in range(1,28124):
    if abundant_num(i) == True:
        abundant_list.add(i)

abundant_list

abundant_sum = set()
def sum_abundant_num(up_limit):
    for i in abundant_list:
        for x in abundant_list:
            if i + x <= up_limit:
                abundant_sum.add(i+x)
            else:
                break 
                
sum_abundant_num(28123)

non_abundant_sums = set(range(1,28124)) - abundant_sum
non_abundant_sums

total_sum = sum(non_abundant_sums)
total_sum