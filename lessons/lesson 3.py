import random
import string


class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance
        self.__password = password

    def login_method(self, login, password):
        if self.login == login and self.__password == password:
            print(f'My balance {self._balance}')
        else:
            print('неверный логин или пароль!!')

    def __get_random_pass(self):
        chart = string.ascii_letters + string.digits
        password = ''.join(random.choice(chart) for _ in range(6))
        return password

ardager = BankAccount('Ardager', '2638', 1000)

# ardager.login_method("Ardager", '2638')
# print(ardager.__dict__)
# print(ardager._BankAccount__password)
# print(ardager)
# print(ardager.login)

from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):
    # Абстрактный метод
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    # pass
    def make_sound(self):
        print('Gaf Gaf')
class Cat(Animal):
    def make_sound(self):
        print('May May')
gufi = Dog()
kiti = Cat()
# gufi.make_sound()
# kiti.make_sound()




class SendOTP(ABC):
    @abstractmethod
    def send_otp_to_phone(self, phone):
        pass

class KGotp(SendOTP):
    def send_otp_to_phone(self, phone):
        data = f'''
            <Phone>{phone}</Phone>
            <Text>Ваш временный пароль: 1234</Text>
        '''
        return data

class RUotp(SendOTP):
    def send_otp_to_phone(self, phone):
        data = {
            'Phone': phone,
            'Text': 'Ваш временный пароль: 1234'
        }
        return data