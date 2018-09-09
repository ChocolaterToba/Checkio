from itertools import product

BOOK = 'ABCDEFGHIJKL0'


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
    result = [[cell[0], str(ind2 + 1)], [cell[0], str(ind2 - 1)],
              [BOOK[ind1 - 1], str(ind3)], [BOOK[ind1 - 1], str(ind3 + 1)],
              [BOOK[ind1 + 1], str(ind3)], [BOOK[ind1 + 1], str(ind3 + 1)]]
    # And then we get rid of the impossible ones.
    return set(i[0] + i[1] for i in result if i[0] != '0' and
               int(i[1]) in range(1, 10) and i[0] + i[1] != cell)


def supply_line(you, depots, enemies):
    # Creating a 'grid' of all possible cells.
    cells = set(i[0] + i[1] for i in list(product(BOOK[:-1], '123456789')))
    # Removing enemy's neighbours.
    for enemy in set(enemies):
        cells.difference_update(get_neighbours(enemy))
        cells.discard(enemy)
    current_cells = {you}
    i = 0
    # Checking whether any of the depots is in current_cells.
    while current_cells.difference(depots) == current_cells:
        i += 1
        # Creating a set of all possible cells that can be reached by i moves.
        new_cells = set()
        for current_cell in current_cells:
            # For each cell, we look if it's neighbours are available.
            for neighbour in get_neighbours(current_cell):
                if neighbour in cells:
                    # The neighbour gets removed to avoid extra branching.
                    cells.remove(neighbour)
                    new_cells.add(neighbour)
        # If no new cells were found, that means that all path are over.
        if not new_cells:
            return None
        current_cells = new_cells
    return i


if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("A3", {"A9", "F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')
