def is_island(tile, island, r):
    if not tile:
        return False
    if tile[0] > 0:
        if [tile[0] - 1, tile[1]] in island:
            return True
        if tile[1] > 0:
            if [tile[0] - 1, tile[1] - 1] in island:
                return True
        if tile[1] < r - 1:
            if [tile[0] - 1, tile[1] + 1] in island:
                return True
    if tile[1] > 0:
        if [tile[0], tile[1] - 1] in island:
            return True
    if tile[1] < r - 1:
            if [tile[0], tile[1] + 1] in island:
                return True
    if tile[0] < r - 1:
            if [tile[0] + 1, tile[1]] in island:
                return True
            if tile[1] > 0:
                if [tile[0] + 1, tile[1] - 1] in island:
                    return True
            if tile[1] < r - 1:
                if [tile[0] + 1, tile[1] + 1] in island:
                    return True
    return False
def checkio(land_map):
    result = []
    for i, row in enumerate(land_map):
        for x, column in enumerate(row):
            if column == 1:
                result += [[i, x]]
    result1 = [[result[0]]]
    a = result.pop(0)
    q = max([len(land_map), len(land_map[0])])
    for i in range(q ** 2):
        for b in range(q):
            for x, tile in enumerate(result):
                for d, island in enumerate(result1):
                    if tile not in island and is_island(tile, island, len(land_map)):
                        result1[d] += [tile]
                        result[x] = []
                    if tile in island:
                        result[x] = []
        for tile in result:
            if tile:
                result1 += [[tile]]
                break
    for i, island in enumerate(result1):
        result1[i] = len(island)
    return sorted(result1)
            
                        
print(checkio([[1,1,1,1,0,1,1,1,1]]))