def life_counter(state, tick_n):
    # Turning tuple into a list
    state = [list(row) for row in state]
    for i in range(tick_n):
        # Adding empty columns and rows on sides if 1 in any of state's sides.
        if any(line[0] for line in state):
            for w in range(len(state)):
                state[w] = [0] + state[w]
        if any(line[-1] for line in state):
            for w in range(len(state)):
                state[w] += [0]
        if any(cell for cell in state[0]):
            state = [[0 for a in range(len(state[0]))]] + state
        if any(cell for cell in state[-1]):
            state += [[0 for a in range(len(state[0]))]]
        new_state = [[] for w in range(len(state))]
        # Aplying game's rules to every single cell
        for row in range(len(state)):
            for col in range(len(state[0])):
                near = 0
                # There's no need to check the state's angular cells(like 0,0).
                # Checking the upper row.
                if not row and col and col < len(state[0]) - 1:
                    near = sum(state[row + r][col + c] for r in range(2)
                               for c in range(-1, 2))
                # Checking the lower row.
                elif row == len(state) - 1 and col and col < len(state[0]) - 1:
                    near = sum(state[row + r][col + c] for r in range(-1, 1)
                               for c in range(-1, 2))
                # Checking other rows.
                elif row and row < len(state) - 1:
                    near = state[row - 1][col] + state[row + 1][col]
                    if col > 0:
                        near += sum(state[row + r][col - 1]
                                    for r in range(-1, 2))
                    if col < len(state[0]) - 1:
                        near += sum(state[row + r][col + 1]
                                    for r in range(-1, 2))
                # Checking if an alive cell will become dead.
                if state[row][col] and near not in [2, 3]:
                    new_state[row] += [0]
                # Checking if a dead cell will become alive.
                elif not state[row][col] and near == 3:
                    new_state[row] += [1]
                else:
                    new_state[row] += [state[row][col]]
        # Removing extra border rows with 0's (needed for optimisation).
        while len(new_state) > 3:
            if not any(item1 or item2 for item1 in new_state[0]
                       for item2 in new_state[1]):
                new_state.pop(0)
            elif not any(item1 or item2 for item1 in new_state[-1]
                         for item2 in new_state[-2]):
                new_state.pop(-1)
            else:
                break
        # Removing extra border columns with 0's (needed for optimisation).
        while len(new_state[0]) > 3:
            if not any(item[0] or item[1] for item in new_state):
                for w in range(len(new_state)):
                    new_state[w] = new_state[w][1:]
            elif not any(item[-1] or item[-2] for item in new_state):
                for w in range(len(new_state)):
                    new_state[w] = new_state[w][:-1]
            else:
                break
        # Changing the old state wiith the new one.
        state = new_state
    # Returning the amount of alive cells left.
    return sum(sum(row) for row in state)