# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
min_value = 5
max_value = 15
indexes = []

for i in range(len(arr)):
    if min_value <= arr[i] <= max_value:
        indexes.append(i)

print(f"Индексы элементов массива, значения которых от {min_value} до {max_value}:")
print(indexes)
