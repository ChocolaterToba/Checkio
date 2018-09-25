def stones(pile, moves):
    losing = list(range(1, min(moves) + 1))
    winning = list(range(min(moves) + 1, pile + 1))
    new_winning = set()
    while pile not in losing:
        for amount in winning:
            if all(amount - move in new_winning | set(winning)
                   for move in moves if amount - move > 0):
                losing += [amount]
                new_winning.update(set(winning[:winning.index(amount)]))
                winning = winning[winning.index(amount) + 1:]
                break
        else:
            break
    return 2 - int(pile in winning)


if __name__ == '__main__':
    print("Example:")
    print(stones(10431,[5,7,8,13,16,21]))