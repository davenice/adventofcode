# A = rock, B = paper, C = scissors
# X = lose, Y = draw, Z = win
# A beats Z (loses to Y)  // A beats C
# C beats Y (loses to X)  // C beats B
# B beats X (loses to Z)  // B beats A

outcomes = [ 'lose', 'draw', 'win' ]
beats = { 'B':'A', 'C':'B', 'A':'C' }
score = 0

with open("Day2/input.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip('\n')
    letters = line.split(sep=' ')
    print(letters)
    mine = his = letters[0]
    outcome = outcomes[ord(letters[1]) - ord('X')]
    if outcome == 'lose':
        # i lost - find him in the keys of the beats list, the value will be me
        hisIndexInListKeys = list(beats.keys()).index(his)
        mine = list(beats.values())[hisIndexInListKeys]
    elif outcome == 'draw':
        # a draw
        score +=3
    else:
        # i win - find him in the values of the beats list, the key will be me
        hisIndexInListValues = list(beats.values()).index(his)
        mine = list(beats.keys())[hisIndexInListValues]
        score += 6
    score += ord(mine) - ord('A') + 1;

print(score)