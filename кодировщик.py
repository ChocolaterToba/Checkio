def encode(message, key):
    book = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    text = []
    #Removing everythind except letters and sigits from message.
    for i in message:
        if i.isdigit():
            text += i
        elif i.isalpha():
            i = i.lower()
            text += [i]
    text1 = []
    i = 0
    #Preparing message for encoding.
    while i < len(text):
        try:
            if text[i] != text[i + 1]:
                text1 += [text[i] + text[i + 1]]
            else:
                if text[i] != 'x':
                    text.insert(i + 1, 'x')
                    text1 += [text[i] + text[i + 1]]
                else:
                    text.insert(i + 1, 'z')
                    text1 += [text[i] + text[i + 1]]
                    text.insert(i + 1, 'z')
                    text1 += [text[i] + text[i + 1]]                
                    i += 2
            i += 2
        except IndexError:
            text1 += [text[-1] + 'z']
            break
    #Creating cipher_table.
    cipher_table = [[], [], [], [], [], []]
    key = list(key)
    key1 = []
    for i in key:
        if i not in key1:
            key1 += [i]
    for i in range(6):
        for x in range(6):
            if len(key1) > 0:
                cipher_table[i] += key1.pop(0)
            else:
                try:
                    while book[0] in key:
                        a = book.pop(0)
                except IndexError:
                    bla = 0
                cipher_table[i] += book.pop(0)
    #Encoding message.
    for i in range(len(text1)):
        for x in range(5):
            a = text1[i][0]
            m = text1[i][1]
            for u in cipher_table:
                if a in u:
                    a = [cipher_table.index(u), u.index(a)]
                    break
            for u in cipher_table:
                if m in u:
                    m = [cipher_table.index(u), u.index(m)]
                    break
            if a[1] == m[1]:
                if a[0] == 5:
                    a = cipher_table[0][a[1]]
                else:
                    a = cipher_table[a[0] + 1][a[1]]
                if m[0] == 5:
                    m = cipher_table[0][m[1]]
                else:
                    m = cipher_table[m[0] + 1][m[1]]
                text1[i] = a + m
                break
            elif a[0] == m[0]:
                if a[1] == 5:
                    a = cipher_table[a[0]][0]
                else:
                    a = cipher_table[a[0]][a[1] + 1]
                if m[1] == 5:
                    m = cipher_table[m[0]][0]
                else:
                    m = cipher_table[m[0]][m[1] + 1]                
                text1[i] = a + m
                break 
            else:
                q = cipher_table[a[0]][m[1]]
                m = cipher_table[m[0]][a[1]]
                text1[i] = q + m
                break
    #Returning message.
    return ''.join(text1)
        
    
def decode(message, key):
    book = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    text = []
    #removing everything except letters and digits from message.
    for i in message:
        if i.isdigit():
            text += i
        elif i.isalpha():
            i = i.lower()
            text += [i]
    text1 = []
    i = 0
    #Praparing message for decoding.
    while i < len(text) - 1:
        if text[i] != text[i + 1]:
            text1 += [text[i] + text[i + 1]]
        else:
            if text[i] != 'x':
                text.insert(i + 1, 'x')
                text1 += [text[i] + text[i + 1]]
            else:
                text.insert(i + 1, 'z')
                text1 += [text[i] + text[i + 1]]
                text.insert(i + 1, 'z')
                text1 += [text[i] + text[i + 1]]                
                i += 2
        i += 2
    if len(text1[-1]) % 2 != 0:
        text1[-1] += 'z'
    #Preparing cipher_table.
    cipher_table = [[], [], [], [], [], []]
    key = list(key)
    key1 = []
    for i in key:
        if i not in key1:
            key1 += [i]
    for i in range(6):
        for x in range(6):
            if len(key1) > 0:
                cipher_table[i] += key1.pop(0)
            else:
                try:
                    while book[0] in key:
                        a = book.pop(0)
                except IndexError:
                    bla = 0
                cipher_table[i] += book.pop(0)
    #Decoding message.
    for i in range(len(text1)):
        for x in range(5):
            a = text1[i][0]
            m = text1[i][1]
            for u in cipher_table:
                if a in u:
                    a = [cipher_table.index(u), u.index(a)]
                    break
            for u in cipher_table:
                if m in u:
                    m = [cipher_table.index(u), u.index(m)]
                    break
            if a[1] == m[1]:
                if a[0] == 0:
                    a = cipher_table[5][a[1]]
                else:
                    a = cipher_table[a[0] - 1][a[1]]
                if m[0] == 0:
                    m = cipher_table[5][m[1]]
                else:
                    m = cipher_table[m[0] - 1][m[1]]
                text1[i] = a + m
                break
            elif a[0] == m[0]:
                if a[1] == 0:
                    a = cipher_table[a[0]][5]
                else:
                    a = cipher_table[a[0]][a[1] - 1]
                if m[1] == 0:
                    m = cipher_table[m[0]][5]
                else:
                    m = cipher_table[m[0]][m[1] - 1]                
                text1[i] = a + m
                break 
            else:
                q = cipher_table[a[0]][m[1]]
                m = cipher_table[m[0]][a[1]]
                text1[i] = q + m
                break
    #Returning decoded message.
    return ''.join(text1)
while True:
    print('Do you want to encode text? y/n')
    if input() == 'y':
        print('Input text')
        message = input()
        print('Input key')
        key = input()
        print(encode(message, key))
    else:
        print('Input text')
        message = input()
        print('Input key')
        key = input()
        print(decode(message, key))
    print('Do you want to quit? y/n')
    if input() == 'y':
        break