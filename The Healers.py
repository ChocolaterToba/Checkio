class Warrior:
    max_health = 50

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence, self.vampirism, self.lance = 0, 0, 0
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


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.lance = 0.5


class Healer(Warrior):
    max_health = 60

    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0

    def heal(self, unit):
        unit.health += 2
        if unit.health > unit.max_health:
            unit.health = unit.max_health


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        for i in range(amount):
            self.units += [unit_type()]


class Battle():
    def fight(self, first_army, second_army):
        first_army.units += [0]
        second_army.units += [0]
        while first_army.units != [0] and second_army.units != [0]:
            if fight(first_army.units[0], second_army.units[0],
                     first_army.units[1], second_army.units[1]):
                second_army.units = second_army.units[1:]
            else:
                first_army.units = first_army.units[1:]
        return first_army.units != [0]


def fight(unit_1, unit_2, unit_3=0, unit_4=0):
    if unit_2.health <= 0:
        unit_2.is_alive = False
        return True
    while unit_1.health > 0:
        if unit_1.attack > unit_2.defence:
            unit_2.health += unit_2.defence - unit_1.attack
            unit_1.health += ((unit_1.attack - unit_2.defence) *
                              unit_1.vampirism)
            # Attacking second_army's second unit (Lancer's ability).
            if unit_4 and type(unit_1).__name__ == 'Lancer':
                unit_4.health -= ((unit_1.attack - unit_2.defence) *
                                  unit_1.lance)
            # Healing first_army's first unit (Healer's ability).
            if type(unit_3).__name__ == 'Healer':
                unit_3.heal(unit_1)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        if unit_2.attack > unit_1.defence:
            unit_1.health += unit_1.defence - unit_2.attack
            unit_2.health += ((unit_2.attack - unit_1.defence) *
                              unit_2.vampirism)
            # Attacking first_army's second unit(Lancer's ability).
            if unit_3 and type(unit_2).__name__ == 'Lancer':
                unit_3.health -= ((unit_2.attack - unit_1.defence) *
                                  unit_2.lance)
            # Healing second_army's first unit (Healer's ability).
            if type(unit_4).__name__ == 'Healer':
                unit_4.heal(unit_2)
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
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
