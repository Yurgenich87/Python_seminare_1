"""
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

b = input('Введите 6-ти значный номер билета: ')
g = int(b[0]) + int(b[1]) + int(b[2])
k = int(b[3]) + int(b[4]) + int(b[5])

if g == k:
    print('Билет счастливый!!!')
else:
    print('Увы, у вас не счастливый билет:(')
