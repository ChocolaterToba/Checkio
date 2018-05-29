def move2048(state, move):
    for k in range(4):
        if move == 'up' or move == 'down':
            line = [row[k] for row in state]
        else:
            line = state[k]
        plus = ['down', 'right']
        while any((line[i] and not line[i + 1] and move in plus) or
                (line[-i - 1] and not line[-i - 2] and move not in plus)
                 for i in range(3)):
            for x in range(3):
                if line[x] and not line[x + 1] and move in plus:
                    line[x], line[x + 1] = line[x + 1], line[x]
                elif line[-x - 1] and not line[-x - 2] and move not in plus:
                    line[-x - 1], line[-x - 2] = line[-x - 2], line[-x - 1]
        for i in range(3):
            if move not in plus:
                if line[i] and line[i] == line[i + 1]:
                    line[i] *= 2
                    line[i + 1] = 0
            else:
                if line[-i - 1] and line[-i - 1] == line[-i - 2]:
                    line[-i - 1] *= 2
                    line[-i - 2] = 0
        while any((line[i] and not line[i + 1] and move in plus) or
                  (line[-i - 1] and not line[-i - 2] and move not in plus)
                  for i in range(3)):
            for x in range(3):
                if line[x] and not line[x + 1] and move in plus:
                    line[x], line[x + 1] = line[x + 1], line[x]
                elif line[-x - 1] and not line[-x - 2] and move not in plus:
                    line[-x - 1], line[-x - 2] = line[-x - 2], line[-x - 1]
        if move == 'up' or move == 'down':
            for q in range(4):
                state[q][k] = line[q]
    if all(state[w][p] for w in range(4) for p in range(4)):
        return [['G','A','M','E'], ['O','V','E','R'],
                ['G','A','M','E'], ['O','V','E','R']]
    if any(state[w][p] == 2048 for w in range(4) for p in range(4)):
        return [['U','W','I','N'], ['U','W','I','N'],
                ['U','W','I','N'], ['U','W','I','N']]
    for s in range(1, 5):
        for a in range(1, 5):
            if state[-s][-a] == 0:
                state[-s][-a] = 2
                break
        else:
            continue
        return state
