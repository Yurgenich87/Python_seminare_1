Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input:
Output: 6
Примечание: Пользователь может вводить значения списка или список задан изначально.

# Первый способ
# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(lst)))

# Второй способ
lst = []
length = int(input('Введите длину списка: '))
for i in range(length):
    n = int(input(f'Введите элемент {i + 1}: '))
    lst.append(n)
print(*lst)

new_lst = []
count = 0
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
        count += 1

print(count)