from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "удар мечом"


class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


class Fighter:
    def __init__(self, name):
        self.name = name

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        return f"{self.name} наносит {self.weapon.attack()}."


class Monster:
    def __init__(self, name):
        self.name = name

    def take_damage(self):
        return f"{self.name} побежден!"


# Демонстрация боя
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч
sword = Sword()
fighter.changeWeapon(sword)
print("Боец выбрал меч")
print(fighter.attack())
print(monster.take_damage())

# Боец выбирает лук
bow = Bow()
fighter.changeWeapon(bow)
print("Боец выбрал лук")
print(fighter.attack())
print(monster.take_damage())




