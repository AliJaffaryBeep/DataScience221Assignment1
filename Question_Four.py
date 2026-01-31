from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

indices = []
for i, v in enumerate(values):
    if v >= x:
        indices.append(i)

print("Sorted list:", values)
print("x:", x)

if indices:
    print("First matching index:", indices[0])
else:
    print("First matching index: none (no values >= x)")
