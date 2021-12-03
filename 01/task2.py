import numpy as np

x = 0
y = 1
z = 2
count = 0

data = np.loadtxt("input.txt")
while z < 1999:
    lower = data[x] + data[y] + data[z]
    higher = data[x + 1] + data[y + 1] + data[z + 1]
    if lower < higher:
        count += 1
    x += 1
    y += 1
    z += 1

print(count)
