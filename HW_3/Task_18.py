# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random


N = int(input('Введите длинну массива:  '))

# lst = [7, 0, 4, 9, 3, 8, 4, 4, 4, 5]
lst = [random.randrange(10) for _ in range(N)]
print(lst)

k = int(input('Введите натуральное число:  '))
for i in lst:
    if i == k:
        print(i)
        x = lst.index(k) - 1
        print(f'Близкий по величине элемент = {lst[x]}')
        break

else:
    print('Такого элемента нет!')

