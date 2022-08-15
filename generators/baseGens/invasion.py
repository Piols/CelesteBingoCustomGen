import random

def genBoardInvasion(json, seed):
    random.seed(seed)
    permutation = [0] * 25
    used = [False] * 13
    for i in range(25):
        permutation[i] = i
    random.seed(seed)
    random.shuffle(permutation)

    positions = [-1] * 25
    currentPosition = 0
    for i in range(25):
        if not used[permutation[i] // 2]:
            used[permutation[i] // 2] = True
            positions[permutation[i]] = currentPosition
            currentPosition += 1

    result = [None] * 26
    for i in range(25):
        if positions[i] != -1:
            a = random.randint(0, len(json[i]) - 1)
            b = random.randint(0, len(json[i]) - 2)
            if b >= a:
                b += 1
            result[positions[i] + 1] = {'name': json[i][a]['name'], 'difficulty': i + 1}
            result[25 - positions[i]] = {'name': json[i][b]['name'], 'difficulty': i + 1}

    return result