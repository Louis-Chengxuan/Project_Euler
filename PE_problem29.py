
sequence = set()

for a in range(2,101):
    for b in range(2,101):
        if a**b not in sequence:
            sequence.add(a**b)


sequence

len(sequence)