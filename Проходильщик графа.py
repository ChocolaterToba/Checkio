from itertools import combinations_with_replacement as comb


def draw(segments):
    lines = [((item[0], item[1]), (item[2], item[3])) for item in segments]
    odd = list({i[w] for i in lines for w in range(2) if len([item for item in lines if i[w] in item]) % 2 == 1})
    if len(odd) > 2:
        return ()
    result = []
    if len(odd) == 2:
        result += [odd[0]]
        dots = comb([line[line.index(odd[0]) - 1] for line in lines if odd[0] in line], 2)
        for i in dots:
            if i in lines:
                print(i, lines)
                result += [i[0]]
                if (i[0], odd[0]) in lines:
                    lines.remove((i[0], odd[0]))
                else:
                    lines.remove((odd[0], i[0]))
                break
        for i in range(len(lines) - 1):
            for line in lines:
                if result[-1] in line and not (len([item for item in lines if odd[1] in item]) == 1 and odd[1] in line):
                    result += [line[line.index(result[-1]) - 1]]
                    lines.remove(line)
                    break
        result += [odd[1]]
    else:
        result = lines[0]
        lines.remove(result)
        for i in range(len(lines) - 1):
            for line in lines:
                if result[-1] in line:
                    result += (line[line.index(result[-1]) -1],)
                    lines.remove(line)
                    break
        result += (result[0],)
    return result
print(draw({(1,1,1,99),(99,99,1,99),(99,99,99,1),(99,1,1,1)}))