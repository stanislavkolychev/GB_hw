#  Представлен список чисел. Определите элементы списка, не имеющие повторений.
#  Сформируйте итоговый массив чисел, соответствующих требованию.
#  Элементы выведите в порядке их следования в исходном списке.
#  Для выполнения задания обязательно используйте генератор

from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [1, 2, 2, 3, 4, 1, 2]
new = [el for el in my_list if my_list.count(el) == 1]
print(new)
