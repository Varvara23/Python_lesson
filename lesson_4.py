# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка \
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random)

import random
import datetime
list_word = ['Вася', 'Петя', 'Илья', 'Ира', 'Антон', 'Лена', 'Катя', 'Света', 'Валерия', 'Константин', 'Аня', 'Николай', 'Дарья', \
             'Арут', 'Евгения', 'Гена', 'Вова', 'Ульяна', 'Игорь', 'Леша']
n = 100

def f(_list_word, _n):
    list_ret = []
    for i in range(_n):
        list_ret.append(random.choice(_list_word))
    return list_ret

list_w = f(list_word, n)
print(list_w)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F

def check(_list_w):
    dict_words = {}
    for k in _list_w:
        dict_words[k] = _list_w.count(k)

    list_words_unic = list(dict_words.items())
    list_words_unic.sort(key=lambda i: i[1])
    list_words_unic.reverse()
    return (list_words_unic[0][0])

print(check(list_w))

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F

def rare(_list_w):
    list_low = []
    for k in _list_w:
        list_low += k[0]
    dict_words = {}
    for i in list_low:
        dict_words[i] = list_low.count(i)

    list_words_unic = list(dict_words.items())
    list_words_unic.sort(key=lambda i: i[1])
    return (list_words_unic[0][0])

print(rare(list_w))

# 4.  В файле с логами найти дату самого позднего лога (по метке времени)

file = open('log', encoding='utf-8')
dt_max = datetime.datetime(1900, 1, 1)  # объявляем нулевую дату 01.01.1900
for line in file:
    dt_log = datetime.datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
    if dt_max < dt_log:
        dt_max = dt_log
        line_max = line
print(line_max)
