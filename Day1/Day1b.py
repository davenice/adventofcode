greediestElves = []
with open("Day1/input.txt") as f:
    lines = f.readlines()
lines.append("\n")

currentElf = 0
for calorie in lines:
    if(len(calorie.strip()) == 0):
        greediestElves.append(currentElf)
        currentElf = 0
    else:
        currentElf += int(calorie)


greediestElves.sort(reverse=True)
print(sum(greediestElves[0:3:]))
