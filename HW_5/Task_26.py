# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a * a, b // 2)
    else:
        return a * power(a, b - 1)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print("{} ** {} = {}".format(a, b, power(a, b)))
