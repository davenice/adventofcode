import string

with open("Day3/input.txt") as f:
    lines = f.readlines()

commonItems=""
total = 0
assert len(lines) % 3 == 0
while (len(lines) >= 3):
    group = lines[0:3]
    allItems = ""
    for bag in group:
        allItems += "".join(set(bag.strip())) # dedup
    # the character that appears 3 times is the one
    badgeLetter = ""
    for letter in group[0].strip():
        if (allItems.count(letter)) == 3:
            badgeLetter = letter
            break

    letterPositions = string.ascii_lowercase + string.ascii_uppercase
    total += letterPositions.find(badgeLetter) + 1
    lines = lines[3:]
print(total)