def nonogram_row(row_string, clue_numbers):
    if not clue_numbers:
        clue_numbers = [0]
    for i in range(len(clue_numbers)):
        part = row_string[sum(clue_numbers[0:i]) + i:
                          i -sum(clue_numbers[i + 1:]) - len(clue_numbers)]
        print(part)
        if 'X' in part:
            ' The string is incorrect.'
            part = part.split('X')
            if len(max(part, key=len)) < clue_numbers[i]:
                return None
            ' There is one good part with 'O' in it
            elif len([a for a in part if 'O' in a and len(a) >= clue_numbers[i]]) == 1:
                for a in range(len(part)):
                    if 'O' in part[a]:
                        part[a] = list(part[a])
                        start = part[a].index('O')
                        for w in (range(start, clue_numbers[i]) +
                                  range(clue_numbers[i], start)):
                            part[a][w] = 'O'
                        part[a] = ''.join(part[a])                                                   
                        break
            elif len([a for a in part if len(a) >= clue_numbers[i]]) == 1:
                for a in range(len(part)):
                    if len(part[a]) >= clue_numbers[i]:
                        part[a] = list(part[a])
                        for w in range(len(part[a]) -clue_numbers[i], clue_numbers[i]):
                            part[a][w] = 'O'
                        part[a] = ''.join(part[a])
            part = 'X'.join(part)

        else:
            continue
        row_string = (row_string[:sum(clue_numbers[0:i]) + i] + part +
                      row_string[i -sum(clue_numbers[i + 1:]) -
                                 len(clue_numbers):])
    print(row_string)
print(nonogram_row('O?X?O?????', [1, 3]))