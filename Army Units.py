class Army:
    def train_swordsman(self, name):
        pass

    def train_lancer(self, name):
        pass

    def train_archer(self, name):
        pass


class Swordsman:
    def __init__(self, spec, name, race):
        self.name, self.spec, self.race = name, spec, race

    def introduce(self):
        return '{} {}, {} swordsman'.format(self.spec, self.name, self.race)


class Lancer:
    def __init__(self, spec, name, race):
        self.name, self.spec, self.race = name, spec, race

    def introduce(self):
        return '{} {}, {} lancer'.format(self.spec, self.name, self.race)


class Archer:
    def __init__(self, spec, name, race):
        self.name, self.spec, self.race = name, spec, race

    def introduce(self):
        return '{} {}, {} archer'.format(self.spec, self.name, self.race)


class AsianArmy(Army):
    def train_swordsman(self, name):
        return Swordsman('Samurai', name, 'Asian')

    def train_lancer(self, name):
        return Lancer('Ronin', name, 'Asian')

    def train_archer(self, name):
        return Archer('Shinobi', name, 'Asian')


class EuropeanArmy(Army):
    def train_swordsman(self, name):
        return Swordsman('Knight', name, 'European')

    def train_lancer(self, name):
        return Lancer('Raubritter', name, 'European')

    def train_archer(self, name):
        return Archer('Ranger', name, 'European')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"
    
    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
