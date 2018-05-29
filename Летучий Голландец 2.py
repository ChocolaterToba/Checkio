import time
start_time = time.time()
def finish_map(regional_map):
    old_grid = []
    grid = list(regional_map)
    # If old_grid == grid, then no cells changed( and no more will).
    while old_grid != grid:
        old_grid = grid[:]
        # Taking each cell...
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                danger_index = 0
                for a in range(-1, 2):
                    for i in range(-1, 2):
                        if row + a >= 0 and col + i >= 0:
                            try:
                                if old_grid[row + a][col + i] == 'X':
                                    danger_index = -10
                                elif (abs(a) != abs(i) and
                                      old_grid[row + a][col + i] == 'D'):
                                    danger_index += 1
                            except:
                                continue
                # Checdking if Flying Dutchman can enter the cell.
                if danger_index > 0:
                    grid[row] = grid[row][:col] + 'D' + grid[row][col + 1:]
    # Replacing all dots with 'S's.
    return tuple(row.replace('.', 'S') for row in grid)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"

print("--- %s seconds ---" % (time.time() - start_time))