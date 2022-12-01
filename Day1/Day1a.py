greediestElf = 0

with open("Day1/input.txt") as f:
    lines = f.readlines()

currentElf = 0
for calorie in lines:
    if(len(calorie.strip()) == 0):
        if (currentElf > greediestElf):
            greediestElf = currentElf
        currentElf = 0
    else:
        currentElf += int(calorie)

print(greediestElf)