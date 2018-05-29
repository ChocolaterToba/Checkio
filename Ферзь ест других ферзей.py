from itertools import chain


BOOK = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def berserk_rook(berserker, enemies):
    ways = [[berserker]]
    # We need one more step to return result.
    for i in range(len(enemies) + 1):
        ways1 = []
        # Taking a single way from ways.
        for way in ways:
            # curr_position is the cell that the rook is on.
            curr_position = way[-1]
            '''In this part the program checks for possibilities of rook
               going up, down, right and left to take another rook.
               'Range' serves as 'if' at the same time, because, if rook
               can't go in some direction, range for that direction will
               be empty and skipped. 'enemies - set(way)' part is needed
               to make sure that taken rooks do not repeat.
            '''
            # Checking for the possibility of going up.
            for i in range(BOOK.index(curr_position[0]) + 1, 8):
                if BOOK[i] + curr_position[1] in enemies - set(way):
                    ways1 += [way + [BOOK[i] + curr_position[1]]]
                    break
            # Checking for the possibility of going down.
            for i in range(BOOK.index(curr_position[0]))[::-1]:
                if BOOK[i] + curr_position[1] in enemies - set(way):
                    ways1 += [way + [BOOK[i] + curr_position[1]]]
                    break
            # Checking for the possibility of going right.
            for i in range(int(curr_position[1]) + 1, 9):
                if curr_position[0] + str(i) in enemies - set(way):
                    ways1 += [way + [curr_position[0] + str(i)]]
                    break
            # Checking for the possibility of going left.
            for i in range(int(curr_position[1]))[::-1]:
                if curr_position[0] + str(i) in enemies - set(way):
                    ways1 += [way + [curr_position[0] + str(i)]]
                    break
        # If ways1 is empty then there are no paths left.
        if not ways1:
            return len(ways[0]) - 1
        ways = ways1[:]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
    assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
    assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"