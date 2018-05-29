def lanterns_flow(river_map, minutes):
    # Getting columns of lanterns' positions.
    lantern_cols = [a for a in range(len(river_map[0]))
                    if river_map[0][a] == '.']
    new_map = [list(a) for a in river_map]
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for lantern in lantern_cols:
        row, col = 0, lantern
        way = 0
        i = minutes
        # Filling lantern's path with Xs.
        while row < len(new_map) - 1 and col < len(new_map[0]) - 1:
            # Adding lantern's position to result if time is over.
            if not i:
                result += [[row, col]]
            new_map[row][col] = 'X'
            # Changing lantern's movement direction.
            while (new_map[row + moves[way - 1][0]][col + moves[way - 1][1]] !=
                   'X' or new_map[row + moves[way][0]][col + moves[way][1]] !=
                   '.'):
                if way == 3:
                    way = 0
                else:
                    way += 1
            # Changing lantern's position.
            row += moves[way][0]
            col += moves[way][1]
            i -= 1
    # Creating a list of lit cells.
    lights = ((lantern[0] + i, lantern[1] + k) for lantern in result
              for i in range(-1, 2) for k in range(-1, 2)
              if river_map[lantern[0] + i][lantern[1] + k] != 'X' and
              lantern[0] + i > -1)
    # Returning len of set of unique cells.
    return len(set(lights))
print(lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 7))