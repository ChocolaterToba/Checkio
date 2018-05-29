def xo_referee(game_result):
    result = 0
    if len(game_result) == 3:
        for x in range(3):
            #Checking horisontal rows.
            if game_result[x][0] == game_result[x][1]:
                if game_result[x][1] == game_result[x][2]:
                    if game_result[x][0] == 'O':
                        result += 1
                    elif game_result[x][0] == 'X':
                        result -= 1
            #Checking vertical rows.
            if game_result[0][x] == game_result[1][x]:
                if game_result[1][x] == game_result[2][x]:
                    if game_result[0][x] == 'O':
                        result += 1
                    elif game_result[0][x] == 'X':
                        result -= 1
            #Checking '\' diagonal.
            if game_result[0][0] == game_result[1][1]:
                if game_result[1][1] == game_result[2][2]:
                    if game_result[0][0] == 'O':
                        result += 1
                    elif game_result[0][0] == 'X':
                        result -= 1
            #Checking '/' diagonal.
            if game_result[0][2] == game_result[1][1]:
                if game_result[1][1] == game_result[2][0]:
                    if game_result[0][2] == 'O':
                        result += 1
                    elif game_result[0][2] == 'X':
                        result -= 1
    else:
        for x in range(4):
            result1 = []
            for i in game_result:
                result1 += [i[x]]
            if game_result[x][0] == game_result[x][1]:
                if game_result[x][1] == game_result[x][2]:
                    if game_result[x][0] == 'X':
                        if game_result[x][3] != game_result[x][0]:
                            result -= 1
                    elif game_result[x][3] != game_result[x][0]:
                        result += 1
            if game_result[x][1] == game_result[x][2]:
                if game_result[x][2] == game_result[x][3]:
                    if game_result[x][1] == 'X':
                        result -= 1
                    else:
                        result += 1
            if result1[1] == result1[2]:
                if result1[2] == result1[3]:
                    if result1[1] == 'X':
                        if result1[0] != result1[1]:
                            result -= 1
                    elif result1[0] != result1[1]:
                        result += 1
            if result1[0] == result1[1]:
                if result1[1] == result1[2]:
                    if result1[1] == 'X':
                        result -= 1
                    else:
                        result += 1
    if result > 0:
        return 'O'
    if result < 0:
        return 'X'
    #If no winners found, returns 'D'.
    return 'D'    
print(xo_referee(['XOO.', '.XOO', 'XXOO', 'XXOX']))