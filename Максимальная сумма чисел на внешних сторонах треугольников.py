from itertools import permutations


def checkio(old_chips):
    # Sorting every triangle.
    new_chips = [sorted(a) for a in old_chips]
    result1 = []
    # Trying to form a hexagon out of different triangles' positions.
    for chips in permutations(new_chips):
        chips = list(chips)
        result = [chips[0]]
        chips.pop(0)
        for s in range(6):
            i = 0
            while i < len(result[-1]):
                for chip in chips:
                    if result[-1][i] in chip:
                        chips.remove(chip)
                        chip = chip[:]
                        chip.remove(result[-1][i])
                        result[-1] = result[-1][:]
                        result[-1].pop(i)
                        result += [chip]
                        i = 0
                        break
                else:
                    i += 1
        # In case of invelid triangle, result
        if len(result) < 6:
            result1 += [0]
        elif result[0][0] in result[-1]:
            result[-1].remove(result[0][0])
            result[0].pop(0)
            result1 += [sum([chip[0] for chip in result])]
        elif result[0][1] in result[-1]:
            result[-1].remove(result[0][1])
            result[0].pop(1)
            result1 += [sum([chip[0] for chip in result])]
        else:
            result1 += [0]
    return max(result1)       
print(checkio([[2,4,6],[1,3,5],[4,6,1],[3,5,2],[2,1,3],[5,4,6]]))