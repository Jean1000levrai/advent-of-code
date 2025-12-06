pos = 50 
count = 0 

with open("passcode.txt", "r") as f:
    rotations = [line.strip() for line in f if line.strip()]

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])

    for _ in range(distance):
        if direction == "R":
            pos = (pos + 1) % 100
        else:  # "L"
            pos = (pos - 1) % 100
        if pos == 0:
            count += 1

print(count)