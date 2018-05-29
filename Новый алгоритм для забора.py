def checkio(required, operations):
    pieces = []
    painted = 0
    i = 0
    while painted < required:
        if i >= len(operations):
            return -1
        painted = 0
        pieces += [operations[i]]
        for w in range(30):
            for v, piece in enumerate(pieces):
                for u, item in enumerate(pieces):
                    if v != u and piece and item:
                        if piece[0] >= item[0] and piece[1] <= item[1]:
                            pieces[v] = []
                        if piece[0] <= item[0] and piece[1] >= item[1]:
                            pieces[u] = []                        
                        elif piece[1] >= item[0] and piece[1] <= item[1]:
                            pieces[v] = [pieces[v][0], item[1]]
                            pieces[u] = []
        while [] in pieces:
            pieces.remove([])
        for piece in pieces:
            painted += piece[1] - piece[0] + 1
        i += 1
    return i
print(checkio(15,[[1,2],[20,30],[25,28],[5,10],[4,21],[1,6]]))