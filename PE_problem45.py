# 1. find triangle number
def triangle_num(n):
    number = n * (n + 1) // 2
    return number

# 2. check pentagonal number
def is_pentagonal(n):
    if ((n * 24 + 1) ** 0.5 + 1) % 6 == 0: 
        return True
    return False

# 3. check hexagonal number
def is_hexagonal(n):
    if ((8 * n + 1) ** 0.5 + 1) % 4 == 0:
        return True
    return False

# 4. find next triangle number

for i in range(286, 1000000):
    numbers = triangle_num(i)
    if is_pentagonal(numbers) and is_hexagonal(numbers):
        print(numbers)
        break
