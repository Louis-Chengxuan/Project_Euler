'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''

def cycle_length(d):
    remainders = {}
    position = 0
    numerator = 1

    while True:
        remainder = numerator % d

        if remainder == 0:
            return len(str(d))
        
        if remainder in remainders:
            return position - remainders[remainder]

        
        else:
            remainders[remainder] = position
        
        numerator *= 10
        position += 1

max_d = 2
max_length = 0
for d in range(2,1000):
    if  cycle_length(d) > max_length:
        max_length = cycle_length(d)
        max_d = d
print (max_d)

