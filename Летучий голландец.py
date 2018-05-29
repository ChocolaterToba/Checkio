def finish_map(regional_map):
    old_grid = []
    grid = list(regional_map)
    # If old_grid == grid, then no cells changed( and no more will).
    while old_grid != grid:
        old_grid = grid[:]
        # Taking each cell...
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # ...And making a list of it's neighbours.
                neighbours = ''
                if row > 0:
                    neighbours += grid[row - 1][col]
                    if col > 0:
                        # Only X's matter, because ship can't go diagonally.
                        if grid[row - 1][col - 1] == 'X':
                            neighbours += grid[row - 1][col - 1]
                    if col < len(grid[0]) - 1:
                        if grid[row - 1][col + 1] == 'X':
                            neighbours += grid[row - 1][col + 1]
                if col > 0:
                    neighbours += grid[row][col - 1]
                if col < len(grid[0]) - 1:
                    neighbours += grid[row][col + 1]
                if row < len(grid) - 1:
                    neighbours += grid[row + 1][col]
                    if col > 0:
                        if grid[row + 1][col - 1] == 'X':
                            neighbours += grid[row + 1][col - 1]
                    if col < len(grid[0]) - 1:
                        if grid[row + 1][col + 1] == 'X':
                            neighbours += grid[row + 1][col + 1]
                # Checdking if Flying Dutchman can enter the cell.
                if 'D' in neighbours and 'X' not in neighbours:
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
