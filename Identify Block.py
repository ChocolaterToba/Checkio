BLOCKS = {'I': [{1, 2, 3, 4}, {1, 5, 9, 13}],
          'J': [{1, 2, 3, 7}, {2, 6, 10, 9}, {1, 5, 6, 7}, {2, 1, 5, 9}],
          'L': [{1, 5, 9, 10}, {5, 1, 2, 3}, {1, 2, 6, 10}, {3, 7, 6, 5}],
          'O': [{1, 2, 5, 6}],
          'S': [{3, 2, 6, 5}, {1, 5, 6, 10}],
          'T': [{1, 2, 3, 6}, {2, 5, 6, 10}, {2, 5, 6, 7}, {1, 5, 6, 9}],
          'Z': [{1, 2, 6, 7}, {2, 6, 5, 9}]}


def identify_block(numbers):
    numbers = list(numbers)
    while not any(number in [1, 5, 9, 13] for number in numbers):
        for i in range(len(numbers)):
            numbers[i] -= 1
    while not any(number in range(1, 5) for number in numbers):
        for i in range(len(numbers)):
            numbers[i] -= 4
    numbers = set(numbers)
    for block in BLOCKS:
        for position in BLOCKS[block]:
            if numbers == position:
                return block
    return None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) is None, 'None'
    print('"Run" is good. How is "Check"?')

    