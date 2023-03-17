'''
Q: It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
# 1. create if_same_number function
def is_Same_number(num):
    set_num = set(str(num))
    for i in range(2, 7):
        if set_num != set(str(i * num)):
            return False
    return True

# 2. find number
for j in range(1,1000000):
    if is_Same_number(j):
        print(j)
    




