import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1

# Дочерние классы с наследованием и полиморфизмом
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} (Воин) атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} (Маг) кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} (Ассасин) атакует!")

# Классы
warrior = Warrior("Конан", 10, 100, 20, stamina=50)
mage = Mage("Гэндальф", 12, 80, 15, mana=100)
assassin = Assassin("Эцио", 11, 85, 18, stealth=90)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

# Камень ножницы и бумага
user_choice = input("Выберите героя (Warrior / Mage / Assassin): ").strip().lower()

if user_choice in heroes:
    player_hero = heroes[user_choice]
    enemy_hero = random.choice(list(heroes.values()))

    print(f"\nВы выбрали: {player_hero.__class__.__name__}")
    print(f"Противник: {enemy_hero.__class__.__name__}")

    p_type = player_hero.__class__.__name__
    e_type = enemy_hero.__class__.__name__

    if p_type == e_type:
        print("Ничья!")
    elif (p_type == "Warrior" and e_type == "Assassin") or \
         (p_type == "Assassin" and e_type == "Mage") or \
         (p_type == "Mage" and e_type == "Warrior"):
        print(f"{p_type} победил!")
    else:
        print(f"{e_type} победил!")
else:
    print("Неверный выбор героя!")