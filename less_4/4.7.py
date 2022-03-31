# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fact_gen(num):
    f_num = 1
    for i in range(num+1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1

for el in fact_gen(int(input('Factorial number: '))):
    print(el)