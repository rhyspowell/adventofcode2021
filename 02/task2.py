forward = 0
depth = 0
aim = 0

with open("input.txt") as f:
    for line in f:
        data = line.split(" ")
        if "forward" in line:
            forward += int(data[1])
            depth += int(data[1]) * aim
        elif "down" in line:
            aim += int(data[1])
        elif "up" in line:
            aim -= int(data[1])
        print(forward, depth, aim)

print(forward)
print(depth)

print(forward * depth)
