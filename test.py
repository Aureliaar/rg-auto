import math
total = 0
valid = 0

numbers = []
for b in range (1, 7):
    for c in range(1, 7):
        numbers.append(b+c)
print(numbers)
print(len(numbers))
for b in numbers: 
    for c in numbers:
        total += 1
        root = (b*b) - (4*c)
        if root >= 0: continue
        print("{}, {} = {}".format(b, c, root))
        valid += 1

print("{}/{}".format(valid, total))