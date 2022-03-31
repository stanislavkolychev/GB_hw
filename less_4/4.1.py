#1 Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary():
    try:
        worked_hour, rate, benefit = map(int, argv[1:])
        print(f"Salary - {worked_hour * rate + benefit}")
    except ValueError:
        print("Enter all 3 num. Not string or empty character")

salary()