# Курсы валют
rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}


class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency.upper()

    # Метод конвертации в сомы
    def convert_to_kgs(self) -> float:
        if self.currency in rates:
            return self.amount * rates[self.currency]
        raise ValueError(f"Неизвестная валюта: {self.currency}")

    #(money1 + money2)
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        # Если валюты одинаковые складываем напрямую
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)

        # Если разные то переводим обе в KGS и складываем
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    # Вычитание (money1 - money2)
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)

        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    # Умножение денег на число (money * 3)
    def __mul__(self, number: float):
        if isinstance(number, (int, float)):
            return Money(self.amount * number, self.currency)
        return NotImplemented

    # Деление денег на число (money / 2)
    def __truediv__(self, number: float):
        if isinstance(number, (int, float)):
            if number == 0:
                raise ZeroDivisionError("Нельзя делить деньги на ноль!")
            return Money(self.amount / number, self.currency)
        return NotImplemented

    # Красивый вывод
    def __str__(self):
        # Округляем до 2 знаков для красоты, если число дробное
        formatted_amount = int(self.amount) if self.amount.is_integer() else round(self.amount, 2)
        return f"{formatted_amount} {self.currency}"


#Проверка работы программы

if __name__ == "__main__":
    money1 = Money(100, "USD")
    money2 = Money(5000, "KGS")

    print(f"Money 1: {money1}")  # 100 USD
    print(f"Money 2: {money2}")  # 5000 KGS

    # Конвертация
    print(f"100 USD в KGS: {money1.convert_to_kgs()} KGS")  # 8900.0 KGS

    # Сложение
    result_add = money1 + money2
    print(f"Сложение (100 USD + 5000 KGS): {result_add}")  # 13900 KGS

    # Вычитание
    result_sub = money1 - money2
    print(f"Вычитание (100 USD - 5000 KGS): {result_sub}")  # 3900 KGS

    # Умножение
    result_mul = money1 * 3
    print(f"Умножение (100 USD * 3): {result_mul}")  # 300 USD

    # Деление
    result_div = money2 / 2
    print(f"Деление (5000 KGS / 2): {result_div}")  # 2500 KGS