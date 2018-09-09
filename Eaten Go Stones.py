def get_dames(stone, rows):
    '''Return all possible dames for stone on a rows*rows board.'''
    dames = []
    if stone[0]:
        dames += [[stone[0] - 1, stone[1]]]
    if stone[0] < rows - 1:
        dames += [[stone[0] + 1, stone[1]]]
    if stone[1]:
        dames += [[stone[0], stone[1] - 1]]
    if stone[1] < rows - 1:
        dames += [[stone[0], stone[1] + 1]]
    return dames


def find_group(stone, stones, rows=9):
    '''Return a stone's group.

    This function finds all stones from 'stones' list that are directly or
    indirectly attached to the 'stone' on a rows*rows board.
    '''
    group = [stone]
    new_group = group[:]
    while True:
        for new_stone in stones:
            if any(dame in new_group for dame in get_dames(new_stone, rows)):
                new_group += [new_stone]
                stones.remove(new_stone)
        # If no new stones were added, return group.
        if new_group == group:
            return group
        group = new_group[:]


def territory(board):
    '''Find the black and white stones' territory.'''
    empty_dames = []
    # Finding all empty dames coordinates.
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '+':
                empty_dames += [[row, col]]
    groups = []
    # Sorting empty dames into groups.
    while empty_dames:
        groups += [find_group(empty_dames[0], empty_dames[1:], len(board))]
        # Removing grouped dames from the list.
        for dame in find_group(empty_dames[0],
                               empty_dames[1:],
                               len(board)):
            empty_dames.remove(dame)
    result = {'B': 0, 'W': 0}
    # Checking for 'trapped' groups of dames without available dames.
    for colour in result:
        for group in groups:
            if all(all(board[dame[0]][dame[1]] in [colour, '+']
                       for dame in get_dames(stone, len(board)))
                   for stone in group):
                result[colour] += len(group)
    return result

if __name__ == '__main__':
    print("Example:")
    print(territory(['++B++++++',
                     '+BB++++++',
                     'BB+++++++',
                     '+++++++++',
                     '+++++++++',
                     '++WWW++++',
                     '++W+W++++',
                     '++WWW++++',
                     '+++++++++']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert territory(['++B++++++',
                      '+BB++++++',
                      'BB+++++++',
                      '+++++++++',
                      '+++++++++',
                      '++WWW++++',
                      '++W+W++++',
                      '++WWW++++',
                      '+++++++++']) == {'B': 3, 'W': 1}
    print("Coding complete? Click 'Check' to earn cool rewards!")
