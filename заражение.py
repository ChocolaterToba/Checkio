def capture(field):
    result = -1
    infected_computers = 0
    while infected_computers < len(field):
        #2 - infected connection, 3 - infecting connection.
        print(field)
        infected_computers = 0
        for column in range(len(field)):
            for a in range(len(field)):
                if column != a:
                    if field[column][a] == 3 or field[a][column] == 3:
                        field[column][column] -= 1
                        break
            if field[column][column] <= 0:
                for a in range(len(field)):
                    if a != column:
                        if field[column][a] == 1:
                            field[column][a] = 2
                        if field[a][column] == 1:
                            field[a][column] = 2
                infected_computers += 1
        for i in range(len(field)):
            for a in range(len(field)):
                if i != a:
                    if field[i][a] == 2:
                        field[i][a] = 3
                    elif field[a][i] == 2:
                        field[a][i] = 3  
        result += 1
    return result