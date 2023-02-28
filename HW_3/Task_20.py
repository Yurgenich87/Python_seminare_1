# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12
def dictionary_english():
    """распределение очков английского алфавита"""
    letters_1 = ('dg')
    cl_1 = dict.fromkeys(letters_1, 2)
    letters_2 = ('bcmp')
    cl_2 = dict.fromkeys(letters_2, 3)
    letters_3 = ('fhvwy')
    cl_3 = dict.fromkeys(letters_3, 4)
    letters_4 = ('k')
    cl_4 = dict.fromkeys(letters_4, 5)
    letters_5 = ('jx')
    cl_5 = dict.fromkeys(letters_5, 8)
    letters_6 = ('qz')
    cl_6 = dict.fromkeys(letters_6, 10)
    cl_english = {**cl_2, **cl_3, **cl_4, **cl_5, **cl_6}
    return cl_english


def dictionary_russia():
    """Распределение очкой русского алфавита"""
    letters_7 = ('авеинорст')
    cl_7 = dict.fromkeys(letters_7, 1)
    letters_8 = ('дклмпу')
    cl_8 = dict.fromkeys(letters_8, 2)
    letters_9 = ('бгёья')
    cl_9 = dict.fromkeys(letters_9, 3)
    letters_10 = ('йы')
    cl_10 = dict.fromkeys(letters_10, 4)
    letters_11 = ('жзчцч')
    cl_11 = dict.fromkeys(letters_11, 5)
    letters_12 = ('шэю')
    cl_12 = dict.fromkeys(letters_12, 8)
    letters_13 = ('фщъ')
    cl_13 = dict.fromkeys(letters_13, 10)
    cl_russia = {**cl_7, **cl_8, **cl_9, **cl_10, **cl_11, **cl_12, **cl_13}
    return cl_russia


combined_dictionary = {**dictionary_english(), **dictionary_russia()}  # Объединение словарей
word = tuple(input('Введите слово:'))
cost = 0
for i in word:
    for j in combined_dictionary:
        if i == j:
            cost += combined_dictionary.get(i)
print(f'Cтоимость введенного слова = {cost}')
