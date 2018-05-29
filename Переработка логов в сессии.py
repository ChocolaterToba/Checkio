def checkio(log_text):
    log = [text.split(';;') for text in log_text.split('\n')]
    for i in range(len(log)):
        log[i][1] = log[i][1].lower()
        log[i][2] = log[i][2].split('/')
        if log[i][2][2].count('.') > 1:
            log[i][2][2] = log[i][2][2][log[i][2][2].index('.') + 1:]
        log[i][2] = log[i][2][2]
    result = []
    for i in log:
        if not result:
            result += [i + [1] + [1]]
        else:
            for k in range(len(result)):
                if (i[1] == result[k][1] and i[2] == result[k][2] and
                    i[0][:10] == result[k][0][:10] and ((int(i[0][11:13]) * 60 +
                    int(i[0][14:16]) - int(result[k][0][11:13]) * 60 -
                    int(result[k][0][14:16])) * 60 + int(i[0][-2:]) - int(result[k][0][-2:])) <= 1800):
                    print(result[k], i)
                    result[k][3] += ((int(i[0][11:13]) * 60 + int(i[0][14:16]) -
                                      int(result[k][0][11:13]) * 60 -
                                      int(result[k][0][14:16])) * 60 +
                                      int(i[0][-2:]) - int(result[k][0][-2:]))
                    result[k][4] += 1
                    result[k][0] = i[0]
                    break
            else:
                result += [i + [1] + [1]]