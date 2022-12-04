import string

with open("Day3/input.txt") as f:
    lines = f.readlines()

commonItems=""
for line in lines:
    line = line.strip()
    assert len(line) % 2 == 0
    midpoint = round(len(line)/2)
    compartmentA = line[0:midpoint]
    compartmentB = line[midpoint:]
    commonItemsForBag = ""
    for item in compartmentA:
        if compartmentB.find(item) != -1:
            commonItemsForBag += item
    commonItems += "".join(set(commonItemsForBag))

total = 0
letterPositions = string.ascii_lowercase + string.ascii_uppercase
for letter in commonItems:
    total += letterPositions.find(letter) + 1

print(total)