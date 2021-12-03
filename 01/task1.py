import numpy as np

x = 0
y = 1
count = 0

data = np.loadtxt("input.txt")
while y < 2000:
    if data[x] < data[y]:
        count += 1
    x += 1
    y += 1

print(count)
