forward = 0
depth = 0

with open("input.txt") as f:
    for line in f:
        print(line)
        if "forward" in line:
            data = line.split(" ")
            print(data)
            forward = forward + int(data[1])
        elif "down" in line:
            data = line.split(" ")
            depth = depth + int(data[1])
        elif "up" in line:
            data = line.split(" ")
            depth = depth - int(data[1])

print(forward)
print(depth)

print(forward * depth)
