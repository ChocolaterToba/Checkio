while True:
    a = int(input('Press [1] to continue or [2] to break : '))
    if a == 1:
        print('Input lowercase letter')
        b = input()
        print('The same letter in uppercase : ', b.upper())
    else:
        break