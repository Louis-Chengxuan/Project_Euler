
r_u = 9
r_d = 3
l_u = 7
l_d = 5

def corner_value(n):
    length = n-1
    r_u = n**2
    l_u = n**2 - length
    l_d = l_u - length
    r_d = l_d - length
    sum = r_u + l_u + l_d + r_d
    return sum

t_sum = 0
for i in range(3,1002,2):
    t_sum += corner_value(i)

t_sum






