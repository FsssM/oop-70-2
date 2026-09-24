from abc import ABC, abstractmethod

#класс Hero
class Hero(ABC):
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    @abstractmethod
    def action(self):
        pass


#Дочерний класс MageHero
class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


# WarriorHero наследуется от MageHero
class WarriorHero(MageHero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


# 3. Класс BankAccount
class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero: Hero, balance: float, password: str):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password: str) -> bool:
        return self.__password == password

    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name}, Уровень: {self.hero.lvl}, Баланс: {self._balance} SOM"

    def get_bank_name(self) -> str:
        return self.bank_name

    def bonus_for_level(self) -> float:
        return self.hero.lvl * 10

    # 4. Магич методы
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return (type(self.hero) is type(other.hero)) and (self.hero.lvl == other.hero.lvl)


#Проверка работы программы

#Герои
mage1 = MageHero("Meliodas", 50, 100, 150)
mage2 = MageHero("Meliodas", 50, 100, 200)
warrior = WarriorHero("Gowther", 50, 200)

# Создаем счета
acc1 = BankAccount(mage1, 5000, "qwerty")
acc2 = BankAccount(mage2, 3000, "12345")
acc3 = BankAccount(warrior, 4000, "admin")

# Вывод действий героев
print(mage1.action())
print(warrior.action())

# Вывод информации о счетах
print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", int(acc1.bonus_for_level()), "SOM")

# Проверка __add__
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

# Проверка __eq__
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)
