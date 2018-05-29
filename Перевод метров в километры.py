while True:
    a = int(input('Press [1] to continue or [2] to exit : '))
    if a == 1:
        print('Input amount of meters')
        a = int(input())
        print(a, 'meters is', a / 1000, 'kilometers.')
    else:
        break