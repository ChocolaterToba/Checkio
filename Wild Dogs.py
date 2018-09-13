from math import sqrt


def in_line(first, second, third):
    '''Return whether the third point is on line defined by 2 points.'''
    # Creating vectors.
    vector_1 = [second[0] - first[0], second[1] - first[1]]
    vector_2 = [third[0] - first[0], third[1] - first[1]]
    # Returning whether or not their x's and y's are proportional.
    return vector_1[0] * vector_2[1] == vector_1[1] * vector_2[0]


def distance(first, second):
    '''Get distance from (0, 0) to line defined by 2 points.'''
    return round(abs(second[0] * first[1] - second[1] * first[0]) /
                 sqrt((second[0] - first[0]) ** 2 +
                      (second[1] - first[1]) ** 2), 2)


def wild_dogs(coords):
    '''Get distance from (0, 0) to line with most points on it.'''
    result = []
    # Taking each possible point...
    for i, first in enumerate(coords):
        # Taking each possible point left...
        for n, second in enumerate(coords[i + 1:]):
            line = [first, second]
            # Taking third possible point...
            for third in coords[i + n + 2:]:
                # And adding it to the line if it fits.
                if in_line(first, second, third):
                    line += [third]
            # Replacing result with line if line is bigger or closer.
            if ((len(line) > len(result) or
                 (len(line) == len(result) and
                  distance(first,  second) < distance(result[0], result[1])))):
                result = line[:]
    # Returning distance between (0, 0) and result.
    return distance(result[0], result[1])

if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(1, 4), (3, 8), (2, 6), (11, 0)]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
