class Warrior:

    def __init__(self):
        self.health = 50
        self.strength = 5
        self.is_alive = True


class Knight(Warrior):

    def __init__(self):
        Warrior.__init__(self)
        self.strength = 7


def fight(unit_1, unit_2):
    while unit_1.health > 0:
        unit_2.health -= unit_1.strength
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.strength
    unit_1.is_alive = False
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False

    print("Coding complete? Let's try tests!")
