def recall_password(cipher_grille, ciphered_password):
    ciphers = []
    listed_password = list(ciphered_password)
    password = ''
    for i in range(len(cipher_grille)):
        g = list(cipher_grille[i])
        for x in range(len(g)):
            if g[x] == 'X':
                ciphers += [[i + 1, x + 1]]
        listed_password[i] = list(ciphered_password[i])
    for x in range(4):
        ciphers.sort(key = lambda z: len(cipher_grille) + z[0])
        for q in range(4):
            for i in range(len(ciphers) - 1):
                if ciphers[i][0] == ciphers[i + 1][0]:
                    if ciphers[i][1] > ciphers[i + 1][1]:
                        s = ciphers[i]
                        ciphers[i] = ciphers[i + 1]
                        ciphers[i + 1] = s
        print(ciphers)
        for i in range(len(ciphers)):
            if ciphers[i][0] > 0 and ciphers[i][1] > 0:
                password += listed_password[ciphers[i][0] - 1][ciphers[i][1] - 1]
            elif ciphers[i][0] > 0 and ciphers[i][1] < 0:
                password += listed_password[ciphers[i][0] - 1][ciphers[i][1]]
            elif ciphers[i][0] < 0 and ciphers[i][1] > 0: 
                password += listed_password[ciphers[i][0]][ciphers[i][1] - 1]
            else:
                password += listed_password[ciphers[i][0]][ciphers[i][1]]
            if listed_password[0][0] == listed_password[0][0].lower():
                s = ciphers[i][0]
                ciphers[i][0] = ciphers[i][1]
                ciphers[i][1] = - s
            else:
                s = ciphers[i][1]
                ciphers[i][1] = ciphers[i][0]
                ciphers[i][0] = - s
    return password
print(recall_password(('X....X', '.X.X..', '.X..X.', '......', '.....X', '......'), ('wyhtge', 'aldcdd', 'yobvmd', 'urhfgt', 'aplrhe', 'fgryhd')))