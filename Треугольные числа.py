def checkio(number):
    m = 1
    while m <= number:
        x = 0
        s = 0
        result = []
        while x <= number:
            if x == number:
                return result
            x += (m+s) * (m+s+1) / 2
            result += [int((m+s) * (m+s+1) / 2)]
            s += 1
        m += 1
    return []
            
                        
print(checkio(64))