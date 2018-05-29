def healthy(grid):
    max_size = 0
    healthy_cell = [0, 0]
    # Taking coordinates of each cell.
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            # Counting the minimum distance between cell and borders.
            distance = min(i, k, len(grid) - i, len(grid[i]) - k)
            # Checking if there are helthy colonies with their size > max.
            for size in range(max_size + 1, distance + 1):
                cell = True
                # Checking cell's surroundings.
                for m in range(-size - 2, size + 2):
                    for p in range(-size - 2, size + 2):
                        row = i + m
                        col = k + p
                        rad = abs(m) + abs(p)
                        '''All of the cells with rad <= size are supposed
                           to be alive and all of the cells with their 
                           rad == size + 1 should be dead.
                        '''
                        try:
                            if ((not ((grid[row][col] and rad <= size) or
                                 (not grid[row][col] and rad == size + 1)) and
                                 rad < size + 2) and row >= 0 and col >= 0):
                                cell = False
                        except IndexError:
                            continue
                # If cell is alive, it becomes our new result.
                if cell:
                    max_size = size
                    healthy_cell = [i, k]
    return healthy_cell
print(healthy((((0,1,0),(1,1,1),(0,1,0)))))