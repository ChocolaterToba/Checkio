def simplify(grid):
    ''' Remove all borderline rows of zeros from the grid.'''
    grid = grid.split('\n')
    while grid[0] == '0' * len(grid[0]):
        grid.pop(0)
    while grid[-1] == '0' * len(grid[-1]):
        grid.pop(-1)
    while all(i[0] == '0' for i in grid):
        for w in range(len(grid)):
            grid[w] = grid[w][1:]
    while all(i[-1] == '0' for i in grid):
        for w in range(len(grid)):
            grid[w] = grid[w][:-1]
    return grid


def turn(grid):
    '''Turn the grid 90 degrees counterclockwise.'''
    return [''.join(row[i] for row in grid) for i in range(len(grid[0]))][::-1]


def keys_and_locks(lock, some_key):
    '''Return whether some_key and lock match.'''
    lock, some_key = simplify(lock), simplify(some_key)
    print(lock, turn(lock))
    for i in range(4):
        if lock == some_key:
            return True
        some_key = turn(some_key)
    return False


if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
                         '''
00000
000##
#####
##000
00000'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
                          '''
00000
000##
#####
##000
00000''')

    assert not keys_and_locks('''
###0
00#0''',
                              '''
00000
00000
#0000
###00
0#000
0#000''')

    assert keys_and_locks('''
0##0
0#00
0000''',
                          '''
##000
#0000
00000
00000
00000''')
    print("Coding complete? Click 'Check' to earn cool rewards!")
