from abc import ABC, abstractmethod

#Родительский класс
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health  # Приватный атрибут (инкапсуляция)
        self.strength = strength

    # Геттер для безопасного получения значения приватного атрибута
    def get_health(self):
        return self.__health

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.__health += 1  # Изменяем приватный атрибут внутри класса

    @abstractmethod
    def attack(self):
        pass


# Дочерние классы
class Warrior(Hero):
    def attack(self):
        print(f"{self.name} — Воин атакует мечом!")


class Mage(Hero):
    def attack(self):
        print(f"{self.name} — Маг использует магию!")


class Assassin(Hero):
    def attack(self):
        print(f"{self.name} — Ассасин атакует из-под тишка!")


#Объекты каждого класса
warrior = Warrior("Гатс", level=10, health=100, strength=20)
mage = Mage("Каска", level=12, health=80, strength=15)
assassin = Assassin("Гриффит", level=11, health=85, strength=18)

# Массив всех героев для удобной проверки
heroes = [warrior, mage, assassin]

#Методы у каждого героя
for hero in heroes:
    print(f"=== {hero.__class__.__name__} ===")
    hero.greet()
    hero.attack()
    print(f"Здоровье до отдыха: {hero.get_health()}")
    hero.rest()
    print(f"Здоровье после отдыха: {hero.get_health()}\n")