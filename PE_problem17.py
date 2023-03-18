def number_to_words(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["onethousand"]

    if n < 10:
        length = len(units[n])
    if 10 <= n < 20:
        length = len(teens[n % 10])
    if 20 <= n < 100:
        length = len(tens[n // 10]) + len(units[n % 10])
    if 100 <= n < 1000:
        if n % 100 == 0:
            length = len(units[n // 100]) + 7
        else:
            length = len(units[n // 100]) + 10 + number_to_words(n % 100)
    if n == 1000:
        length = len(thousands[0])
    
    return length


sum_num = 0
for i in range(1,1001):
    sum_num += number_to_words(i)
print(sum_num)


