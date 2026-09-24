# # # магичекский метод
# # #__init__
# #
# # # | Метод         | Что делает                |
# # # | ------------- | ------------------------- |
# # # | `__init__`    | конструктор               |
# # # | `__str__`     | вывод через `print()`     |
# # # | `__repr__`    | отображение объекта       |
# # # | `__len__`     | `len(obj)`                |
# # # | `__getitem__` | `obj[key]`                |
# # # | `__call__`    | вызов объекта как функции |
# # # | `__eq__`      | `==`                      |
# # # | `__lt__`      | `<`                       |
# # # | `__gt__`      | `>`                       |
# #
# #
# # # | Оператор | Магический метод | Пример   |
# # # | -------- | ---------------- | -------- |
# # # | `+`      | `__add__`        | `a + b`  |
# # # | `-`      | `__sub__`        | `a - b`  |
# # # | `*`      | `__mul__`        | `a * b`  |
# # # | `/`      | `__truediv__`    | `a / b`  |
# # # | `//`     | `__floordiv__`   | `a // b` |
# # # | `%`      | `__mod__`        | `a % b`  |
# #
# class Test:
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return self.value
#     # def __add__(self, other):
#     #     print(self.value)
#     #     print(other.value)
#     def __getitem__(self, item):
#         return self.value[item]
# #
# #     def __call__(self, *args, **kwargs):
# #         self.value += 1
# #         print("+1 вызов!!")
# #         print(self.value)
# #
# #
# test_view = Test(0)
# test_view_2 = Test(test_view)
# # # test_view()
# # # test_view()
# # # test_view()
# # # test_view()
# #
# #
# # # my_list = Test([1,2,3,4,5,6])
# # # print(my_list[1])
# # #
# # # my_obj = Test('Test text')
# # # my_str = str("My str")
# # # # print(my_obj)
# # # # print(my_str)
# # #
# # # my_int = Test(123)
# # # my_int_2 = Test(321)
# # # # my_int_3 = my_int + my_int_2
# # # # print(my_int_3)
# #
# # class Money:
# #     def __init__(self, value, currency):
# #         self.value = value
# #         self.currency = currency
# #
# #     # def __converter(self):
# #
# #     def __add__(self, other):
# #         if self.currency == other.currency:
# #             return self.value + other.value
# #         else:
# #
# #             return "Ошибка!!"
# #
# # usd = Money(100, 'USD')
# # som = Money(100, "SOM")
# # # total_money = usd + som
# #
# #
# #
# #
# #
#
#
# # class Math:
# #     def __init__(self, value):
# #         self.value = value
# #
# #     @staticmethod
# #     def added_two_int(a,b):
# #         return a + b
#
# # test_obj = Math("fghjk")
# # print(Math.added_two_int(12, 12))
# # print(test_obj.added_two_int(12, 12))
#
#
# class Bank:
#     # Атрибуты класса
#     bank_name = "Kompanion"
#
#     def __init__(self, capital):
#         # Атрибуты экземпляра класса
#         self.capital = capital
#
#     # public
#     def get_capital(self):
#         return self.capital
#
#     # Protected
#     # def _protected(self):
#     #Private
#     # def __private(self):
#
#     # Abstractmethod
#     # @abstractmethod
#     # def abstractmethod
#
#     # Static
#     # @staticmethod
#     # def static_method():
#
#     # Class method
#     # @classmethod
#     # def get_bank_name(cls):
#     #     return cls.bank_name
#
# # test = Bank(34567890)
# # test_2 = Bank(100)
# # print(test.get_bank_name())
# # print(test_2.get_bank_name())
# # print(Bank.get_bank_name())

from abc import ABC, abstractmethod

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self._last_name = last_name

    # @abstractmethod

    @property
    def full_name(self):
        return f"{self._last_name} {self.first_name}"

    @full_name.setter
    def full_name(self, value):
        self.first_name = value

    @property
    def last_name(self):
        return self._last_name




ardager = User("Ardager", "Kartanbekov")
arzy = User("Arzy", "Abdy")

# print(ardager.first_name)
# ardager.first_name = "TEST"
# print(ardager.first_name)
# print(ardager.last_name)
# print(ardager.full_name)
# ardager.full_name = "TEST"
# print(ardager.full_name)
# print(ardager.last_name)