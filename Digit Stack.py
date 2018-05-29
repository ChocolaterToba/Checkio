def checkio(message):
    result = ''
    for i in message:
        i = list(bin(i))
        x = i.pop(-1)
        if ((x == '0' and i.count('1') % 2 == 0)
            or (x == '1' and i.count('1') % 2 != 0)) :
            i = ''.join(i)
            i = int(i, 2)
            result += chr(i)
    return result
    
print(checkio([160, 243, 232, 209, 222, 221]))