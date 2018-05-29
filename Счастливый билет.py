from itertools import product


O_BRACKETS = ['(' * i for i in range(6)][::-1]
C_BRACKETS = [')' * i for i in range(6)]
OP = ['+', '', '-', '*', '/']
def checkio(data):
    new_data = list(data)
    between = []
    for a in range(1, 6):
        between += [[''.join(q) for q in product(C_BRACKETS[:a], OP,
                                                O_BRACKETS[a:])]]
    print(between)
    for i in product(O_BRACKETS, between[0], between[1], between[2],
                     between[3], between[4], C_BRACKETS):
        try:
            if eval(''.join(zip(i, new_data))) == 100:
                return False
        except:
            continue
    return True

print(checkio('595347'))     