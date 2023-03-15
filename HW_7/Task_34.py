# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в
# его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

# def count_vowels(word):
#     vowels = "aeiouyAEIOUY"
#     count = 0
#     for letter in word:
#         if letter in vowels:
#             count += 1
#     return count
#
#
# poem = input("Введите стихотворение Винни-Пуха: ")
# phrases = poem.split()
# vowel_counts = []
#
# for phrase in phrases:
#     words = phrase.split('-')
#     vowel_counts_in_phrase = [count_vowels(word) for word in words]
#     if len(set(vowel_counts_in_phrase)) != 1:
#         print("Пам парам")
#         break
#     vowel_counts.append(vowel_counts_in_phrase[0])
#
# if len(set(vowel_counts)) == 1:
#     print("Парам пам-пам")

vowels = 'аеёиоуыэюя'
poem = input("Введите стихотворение: ").lower()
phrases = poem.split()
syllables = []

for phrase in phrases:
    words = phrase.split('-')
    syllable_count = sum(sum(1 for c in word if c in vowels) for word in words)
    syllables.append(syllable_count)

if len(set(syllables)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
