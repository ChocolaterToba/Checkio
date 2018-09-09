class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0
        self.is_alive = True


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):

    def __init__(self):
        self.health, self.attack = 60, 3
        self.defence, self.is_alive = 2, True


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
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        if unit_2.attack > unit_1.defence:
            unit_1.health += unit_1.defence - unit_2.attack
    unit_1.is_alive = False
    return False