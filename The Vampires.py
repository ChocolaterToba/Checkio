class Warrior:
    max_health = 50

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence, self.vampirism = 0, 0
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    max_health = 60

    def __init__(self):
        super().__init__()
        self.health, self.attack = 60, 3
        self.defence, self.is_alive = 2, True


class Vampire(Warrior):
    max_health = 40

    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


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
        if unit_1.attack > unit_2.defence:
            unit_2.health += unit_2.defence - unit_1.attack
            unit_1.health += ((unit_1.attack - unit_2.defence) *
                              unit_1.vampirism)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        if unit_2.attack > unit_1.defence:
            unit_1.health += unit_1.defence - unit_2.attack
            unit_2.health += ((unit_2.attack - unit_1.defence) *
                              unit_2.vampirism)
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
