from math import floor


class Warrior:
    max_health = 50

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense, self.vampirism = 0, 0

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack
        if self.attack < 0:
            self.attack = 0
        if type(self).__name__ == 'Defender':
            self.defense += weapon.defense
            if self.defense < 0:
                self.defense = 0
        if type(self).__name__ == 'Vampire':
            self.vampirism += weapon.vampirism
            if self.vampirism < 0:
                self.vampirism = 0
        if type(self).__name__ == 'Healer':
            self.heal_power += weapon.heal_power
            if self.heal_power < 0:
                self.heal_power = 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    max_health = 60

    def __init__(self):
        super().__init__()
        self.health, self.attack = 60, 3
        self.defense = 2


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


class Healer(Warrior):
    max_health = 60

    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0
        self.heal_power = 2

    def heal(self, unit):
        unit.health += self.heal_power
        if unit.health > unit.max_health:
            unit.health = unit.max_health


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        for i in range(amount):
            self.units += [unit_type()]


class Weapon():
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health, self.attack, self.defense = health, attack, defense
        self.vampirism, self.heal_power = vampirism / 100, heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__(5, 2, 0, 0, 0)


class Shield(Weapon):
    def __init__(self):
        super().__init__(20, -1, 2, 0, 0)


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(-15, 5, -2, 10, 0)


class Katana(Weapon):
    def __init__(self):
        super().__init__(-20, 6, -5, 50, 0)


class MagicWand(Weapon):
    def __init__(self):
        super().__init__(30, 3, 0, 0, 3)


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

    def straight_fight(self, army_1, army_2):
        while army_1.units and army_2.units:
            for i in range(min(len(army_1.units), len(army_2.units))):
                if fight(army_1.units[i], army_2.units[i]):
                    army_2.units[i] = 0
                else:
                    army_1.units[i] = 0
            while 0 in army_1.units:
                army_1.units.remove(0)
            while 0 in army_2.units:
                army_2.units.remove(0)
        return bool(army_1.units)


def fight(unit_1, unit_2, unit_3=0, unit_4=0):
    if not unit_2.is_alive:
        return True
    while unit_1.is_alive:
        if unit_1.attack > unit_2.defense:
            unit_2.health += unit_2.defense - unit_1.attack
            unit_1.health += floor((unit_1.attack - unit_2.defense) *
                                   unit_1.vampirism)
            # Attacking second_army's second unit (Lancer's ability).
            if unit_4 and type(unit_1).__name__ == 'Lancer':
                unit_4.health -= (unit_1.attack - unit_2.defense) * 0.5
            # Healing first_army's first unit (Healer's ability).
            if type(unit_3).__name__ == 'Healer':
                unit_3.heal(unit_1)
        if not unit_2.is_alive:
            return True
        if unit_2.attack > unit_1.defense:
            unit_1.health += unit_1.defense - unit_2.attack
            unit_2.health += floor((unit_2.attack - unit_1.defense) *
                                   unit_2.vampirism)
            # Attacking first_army's second unit(Lancer's ability).
            if unit_3 and type(unit_2).__name__ == 'Lancer':
                unit_3.health -= (unit_2.attack - unit_1.defense) * 0.5
            # Healing second_army's first unit (Healer's ability).
            if type(unit_4).__name__ == 'Healer':
                unit_4.heal(unit_2)
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    ogre.health == 125
    lancelot.attack == 17
    richard.defense == 4
    eric.vampirism == 200
    freelancer.health == 15
    priest.heal_power == 5

    assert not fight(ogre, eric)
    assert not fight(priest, richard)
    assert fight(lancelot, freelancer)

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    battle.fight(my_army, enemy_army)
    print("Coding complete? Let's try tests!")
