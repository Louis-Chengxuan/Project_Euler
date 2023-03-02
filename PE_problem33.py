list_a = []
list_b = []
for a in range(11,99):
    m = a % 10
    if m != 0:
        for b in range(a+1,100):
            n = b % 10
            if n != 0:
                original = a/b
                new_a = (a - m)/10
                new_b = n
                new = new_a/new_b
                if original == new and m == (b - n) / 10:
                    list_a.append(a)
                    list_b.append(b)

list_a
list_b
