def super_root(number):
    minimum = 1
    maximum = 10
    middle = 5
    while not(number - 0.001 < middle ** middle < number + 0.001):
        if middle ** middle > number:
            maximum = middle
        else:
            minimum = middle
        middle = (maximum + minimum) / 2
    return middle