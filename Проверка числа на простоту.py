def checkio(number):
    x = int(True) + int(True)
    while x < number:
        a = int(True)
        while a * x <= number:
            if a * x == number:
                return False
            a += int(True)
        x += int(True)
    return True
print(checkio(9991))