def checkio(required, operations):
    wall = []
    operation = []
    for n in operations:
        operation += [n[1]]
    for i in range(max(operation)):
        wall += [0]
    for w in range(len(operations)):
        for x in range(operations[w][0] - 1, operations[w][1]):
            wall[x] = 1
        result = 0
        for a in wall:
            if a == 1:
                result += 1
        if result >= required:
            return w + 1
    return -1
print(checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]))