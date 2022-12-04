# A = rock, B = paper, C = scissors
# X = rock, Y = paper, Z = scissors
# A beats Z (loses to Y)  // A beats C
# C beats Y (loses to X)  // C beats B
# B beats X (loses to Z)  // B beats A

beats = { 'B':'X', 'C':'Y', 'A':'Z' }
equivalence = { 'A':'X', 'B':'Y', 'C':'Z' }
score = 0

with open("Day2/input.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip('\n')
    letters = line.split(sep=' ')
    print(letters)
    his = letters[0]
    mine = letters[1]
    score += list(beats.values()).index(mine) + 1
    if beats[his] == mine:
        # i lost
        print("i lost")
    elif equivalence[his] == mine:
        # a draw
        print("draw")
        score +=3
    else:
        print("i won")
        score += 6


print(score)