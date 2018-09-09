BOOK = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0'
DIRECTIONS = ['N', 'NE', 'SE', 'S', 'SW', 'NW']


def get_neighbours(cell):
    '''Find all the neighbours of cell on the hex grid.'''
    # ind1 showes(by number) which column is our cell in.
    ind1 = BOOK.index(cell[0])
    # ind2 showes which 'row' is our cell ind.
    ind2 = int(cell[1])
    # ind3 is needed to find neighbours from neargy columns.
    ind3 = ind2
    # if the column's number is even, then all neighbours' rows decrease by 1.
    if not ind1 % 2:
        ind3 = ind2 - 1
    # This section makes all possible neighbours...
    result = [[cell[0], str(ind2 - 1), 0], [cell[0], str(ind2 + 1), 3],
              [BOOK[ind1 + 1], str(ind3), 1],
              [BOOK[ind1 + 1], str(ind3 + 1), 2],
              [BOOK[ind1 - 1], str(ind3 + 1), 4],
              [BOOK[ind1 - 1], str(ind3), 5]]
    # And then we get rid of the impossible ones, making a 'circle' by sorting.
    return sorted([[i[0] + i[1], i[2]] for i in result if i[0] != '0' and
                   int(i[1]) in range(10) and i[0] + i[1] != cell],
                  key=lambda x: x[1])


def find_enemy(you, dir, enemy):
    # 'dir' coefficient is needed to adjust directions later.
    dir = DIRECTIONS.index(dir)
    # Getting the first cell from sector 'forward'.
    f_group = [i[0] for i in get_neighbours(you) if i[1] == dir]
    # Getting the first cell from sector 'right'.
    r_group = [i[0] for i in get_neighbours(you) if i[1] in [(dir + 1) % 6,
                                                             (dir + 2) % 6]]
    # Getting the first cell from sector 'backward'.
    b_group = [i[0] for i in get_neighbours(you) if i[1] == (dir + 3) % 6]
    # Getting the first cell from sector 'left'.
    l_group = [i[0] for i in get_neighbours(you) if i[1] in [(dir + 4) % 6,
                                                             (dir + 5) % 6]]
    # f, r, b, l are distances to enemy.
    f, r, b, l = 1, 1, 1, 1
    while f_group:
        # Checking if enemy's cell is ih the sector.
        if enemy in f_group:
            return ['F', f]
        new_group = []
        f += 1
        # Finding new cells from sector.
        for cell in f_group:
            for new_cell in get_neighbours(cell):
                # 0, 1, 5 are encoded positions of adjacent cells.
                if (((new_cell[1] - dir + 6) % 6 in [0, 1, 5] and
                     new_cell[0] not in new_group)):
                    new_group += [new_cell[0]]
        f_group = new_group[:]
    # Basically like f_group but the position of cells adjusted changes.
    while r_group:
        if enemy in r_group:
            return ['R', r]
        new_group = []
        r += 1
        for cell in r_group:
            for new_cell in get_neighbours(cell):
                if (((new_cell[1] - dir + 6) % 6 in [1, 2] and
                     new_cell[0] not in new_group)):
                    new_group += [new_cell[0]]
        r_group = new_group[:]
    while b_group:
        if enemy in b_group:
            return ['B', b]
        new_group = []
        b += 1
        for cell in b_group:
            for new_cell in get_neighbours(cell):
                if (((new_cell[1] - dir + 6) % 6 in [2, 3, 4] and
                     new_cell[0] not in new_group)):
                    new_group += [new_cell[0]]
        b_group = new_group[:]
    while l_group:
        if enemy in l_group:
            return ['L', l]
        new_group = []
        l += 1
        for cell in l_group:
            for new_cell in get_neighbours(cell):
                if (((new_cell[1] - dir + 6) % 6 in [4, 5] and
                     new_cell[0] not in new_group)):
                    new_group += [new_cell[0]]
        l_group = new_group[:]


if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
