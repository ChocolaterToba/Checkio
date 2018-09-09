from math import floor


class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.attack = 5
        self.defense = 0

    @property
    def is_alive(self):
        return self.health > 0

    def assault(self, unit):
        if unit.defense < self.attack:
            unit.health -= self.attack - unit.defense
            if type(self).__name__ == 'Vampire':
                self.health += floor((self.attack - unit.defense) *
                                     self.vampirism)
                if self.health > self.max_health:
                    self.health = self.max_health

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.max_health += weapon.health
        self.attack += weapon.attack
        if self.attack < 0:
            self.attack = 0
        if type(self).__name__ in ['Defender', 'Warlord']:
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


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 1


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health, self.attack = 60, 3
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 40
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6

    def lance_assault(self, unit_1, unit_2):
        if self.attack > unit_1.defense:
            unit_2.health -= (self.attack - unit_1.defense) * 0.5


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health = 60
        self.attack = 0
        self.heal_power = 2

    def heal(self, unit):
        unit.health += self.heal_power
        if unit.health > unit.max_health:
            unit.health = unit.max_health


class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = 100
        self.attack = 4
        self.defense = 2


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, amount):
        if unit_type.__name__ != 'Warlord':
            for i in range(amount):
                self.units += [unit_type()]
        else:
            for unit in self.units:
                if type(unit).__name__ == 'Warlord':
                    break
            else:
                self.units += [Warlord()]

    def move_units(self):
        if type(self.units[-1]).__name__ != 'Warlord':
            for i in self.units:
                if type(i).__name__ == 'Warlord':
                    self.units.remove(i)
                    self.units += [i]
                    break
        for n in range(int((len(self.units) - 1) * len(self.units) / 2)):
            for a in range(len(self.units) - 2):
                if ((type(self.units[a]).__name__ != 'Lancer' and
                     type(self.units[a + 1]).__name__ == 'Lancer')):
                    extra = self.units[a]
                    self.units[a] = self.units[a + 1]
                    self.units[a + 1] = extra
        if len(self.units) > 1:
            if not self.units[1].is_alive:
                self.units.pop(1)
        for n in range(int((len(self.units) - 1) * len(self.units) / 2)):
            for i in range(1, len(self.units) - 2):
                if ((type(self.units[i]).__name__ != 'Healer' and
                     type(self.units[i + 1]).__name__ == 'Healer')):
                    extra = self.units[i]
                    self.units[i] = self.units[i + 1]
                    self.units[i + 1] = extra
        if not self.units[0].is_alive:
            self.units.pop(0)
            for unit in self.units[:-1]:
                if type(unit).__name__ == 'Lancer':
                    self.units.remove(unit)
                    self.units = [unit] + self.units
                    break
            else:
                for unit in self.units[:-1]:
                    if type(unit).__name__ not in ['Healer', 'Warlord']:
                        self.units.remove(unit)
                        self.units = [unit] + self.units
                        break

    def fight_with(self, enemy):
        front_1 = self.units[0]
        front_2 = enemy.units[0]
        if len(self.units) > 1:
            back_1 = self.units[1]
        if len(enemy.units) > 1:
            back_2 = enemy.units[1]
        front_1.assault(front_2)
        if type(front_1).__name__ == 'Lancer' and len(enemy.units) > 1:
            front_1.lance_assault(front_2, back_2)
        if len(self.units) > 1:
            if type(back_1).__name__ == 'Healer':
                back_1.heal(front_1)
        if len(enemy.units) > 1:
            if not(front_2.is_alive and back_2.is_alive):
                if type(enemy.units[-1]).__name__ == 'Warlord':
                    enemy.move_units()
                else:
                    if not front_2.is_alive:
                        enemy.units.remove(front_2)
                        return True
                    if not back_2.is_alive:
                        enemy.units.remove(back_2)
        elif not front_2.is_alive:
            enemy.units.remove(front_2)
            return True
        else:
            return False
        


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
        for unit in first_army.units:
            if type(unit).__name__ == 'Warlord':
                first_army.move_units()
                break
        for unit in second_army.units:
            if type(unit).__name__ == 'Warlord':
                second_army.move_units()
                break  
        while first_army.units and second_army.units:
            if first_army.fight_with(second_army):
                continue
            if not second_army.units:
                return True
            second_army.fight_with(first_army)
        return bool(first_army.units)
                    
            
    def straight_fight(self, army_1, army_2):
        for unit in army_1.units:
            if type(unit).__name__ == 'Warlord':
                army_1.move_units()
                break
        for unit in army_2.units:
            if type(unit).__name__ == 'Warlord':
                army_2.move_units()
                break
        while army_1.units and army_2.units:
            if type(army_1.units[-1]).__name__ == 'Warlord':
                army_1.move_units()
            if type(army_2.units[-1]).__name__ == 'Warlord':
                army_2.move_units()
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


def fight(unit_1, unit_2):
    if not unit_2.is_alive:
        return True
    while unit_1.is_alive:
        unit_1.assault(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.assault(unit_1)
    return False


army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 3)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 4)
army_2.add_units(Warlord, 1)
army_2.add_units(Vampire, 1)
army_2.add_units(Rookie, 1)
army_2.add_units(Knight, 1)
army_1.units[0].equip_weapon(Sword())
army_2.units[0].equip_weapon(Shield())
army_1.move_units()
army_2.move_units()
battle = Battle()
print(battle.straight_fight(army_1, army_2))