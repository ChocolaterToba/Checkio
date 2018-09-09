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


def go_game(board):
    '''Find all stones that will be 'trapped' by enemy's stones.'''
    stones = {'B': [], 'W': []}
    # Finding all black and white stones' coordinates.
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] in stones:
                stones[board[row][col]] += [[row, col]]
    groups = {'B': [], 'W': []}
    # Sorting stones into groups.
    for colour in stones:
        while stones[colour]:
            groups[colour] += [find_group(stones[colour][0],
                               stones[colour][1:],
                               len(board))]
            # Removing grouped stones from the list.
            for stone in find_group(stones[colour][0],
                                    stones[colour][1:],
                                    len(board)):
                stones[colour].remove(stone)
    result = {'B': 0, 'W': 0}
    # Checking for 'trapped' groups without available dames.
    for colour in result:
        for group in groups[colour]:
            if all(all(board[dame[0]][dame[1]] != '+'
                       for dame in get_dames(stone, len(board)))
                   for stone in group):
                result[colour] += len(group)
    return result
    
    

if __name__ == '__main__':
    print("Example:")
    print(go_game(['++++W++++',
                   '+++WBW+++',
                   '++BWBBW++',
                   '+W++WWB++',
                   '+W++B+B++',
                   '+W+BWBWB+',
                   '++++BWB++',
                   '+B++BWB++',
                   '+++++B+++']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert go_game(['++++W++++',
                    '+++WBW+++',
                    '++BWBBW++',
                    '+W++WWB++',
                    '+W++B+B++',
                    '+W+BWBWB+',
                    '++++BWB++',
                    '+B++BWB++',
                    '+++++B+++']) == {'B': 3, 'W': 4}
    print("Coding complete? Click 'Check' to earn cool rewards!")
