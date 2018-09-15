from functools import lru_cache


# lru_cache saves a LOT of execution time.
@lru_cache(maxsize=None)
def probability(dice_number, sides, target):
    result = 0
    # Checking for cases when we only have 1 die.
    if dice_number == 1:
        if target in range(1, sides + 1):
            return 1 / sides
        return 0
    # For each result of throwing the first die...
    # ...we count the possibility of getting the target usingrecursion.
    result = sum(probability(dice_number - 1, sides, target - i - 1) /
                 sides for i in range(sides))
    return result

if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
print('Done')
