'''
Q: Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

# 1. cwd
import os
cwd = os.getcwd()
print(cwd)

# 2. get file
with open('PE_problem22_text.txt', 'r') as file:
    content = file.read()

names = content.strip().split(',')

print(names[:10])
names.sort()

# 3. number of alphabet
def char_to_number(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1

# 4. get answer
time = 1
sum_cnt = 0
for i in names:
    cnt = 0
    for j in range(1, len(i) - 1):
        cnt += char_to_number(i[j])
    cnt *= time
    sum_cnt += cnt
    time += 1

print(sum_cnt)

