# Эта библиотека нужна для раскрашивания текста в консоли (терминале).
# Она позволяет изменять цвет шрифта, фоновый цвет и стиль текста при выводе через print().
from colorama import Fore, Back, Style, init

# Инициализация colorama (обязательна для корректной работы на Windows)
init(autoreset=True)

def main():
    print(Fore.GREEN + "=== Программа успешно запущена ===")
    print(Fore.YELLOW + "Тестирование работы библиотеки colorama...")
    print(Fore.RED + Style.BRIGHT + "Пример вывода ошибки красным цветом!")
    print(Back.BLUE + Fore.WHITE + " Пример текста с синим фоном ")

if __name__ == "__main__":
    main()