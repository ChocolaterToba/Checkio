class Warrior:

    def __init__(self):
        self.health = 50
        self.strength = 5
        self.is_alive = True


class Knight(Warrior):

    def __init__(self):
        Warrior.__init__(self)
        self.strength = 7


class Army():

    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        for i in range(amount):
            self.units += [unit_type()]


class Battle():

    def fight(self, first_army, second_army):
        while first_army.units and second_army.units:
            if fight(first_army.units[0], second_army.units[0]):
                second_army.units = second_army.units[1:]
            else:
                first_army.units = first_army.units[1:]
        return first_army.units != []


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

    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True
    assert battle.fight(army_3, army_4) is False
    print("Coding complete? Let's try tests!")
