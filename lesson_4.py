# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random)
import random
list_word = ['Вася', 'Петя', 'Илья', 'Ира', 'Антон', 'Лена', 'Катя', 'Света', 'Валерия', 'Константин', 'Аня', 'Николай', 'Дарья', 'Арут', 'Евгения', 'Гена', 'Вова', 'Ульяна', 'Игорь', 'Леша']
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
    # print(list_words_unic[:1])
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
    # print(list_words_unic[:1])
    return (list_words_unic[0][0])

print(rare(list_w))
