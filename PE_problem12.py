
def find_triangle_num(n):
    return (n*(n+1))//2

def main(limit_divisors):
    div = 1
    num = 0
    while div <= limit_divisors:
        list = []
        num += 1
        for i in range (1,int(find_triangle_num(num)**0.5) + 1):
            if find_triangle_num(num) % i ==0:
                list.append(2)
        div = len(list)*2 
    return find_triangle_num(num)


main(500) 