file = open('text.txt', encoding='utf-8')  # открытие файла
list_words = []   # список для слов
list_punct = [',','.','!','?','-','—',';',':','«','»','(',')','\n','  ']  # список знаков пунктуации
for line in file:  # цикл для построчного чтения файлов
    for i in list_punct:  # цикл перебора знаков пунктуации
        line = line.replace(i, '')  # удаление значения из строки
    print(line)  # 1) методами строк очистить текст от знаков препинания

    list_words += line.split(' ')  # заполняем список словами из теста текущей строки
print(list_words)  # 2) сформировать list со словами (split)

list_words = list(map(lambda x: x.lower(), list_words))  # перевод слов в нижний регистр
print(list_words)  # 3) привести все слова к нижнему регистру (map)

dict_words = {}  # словарь для подсчета слов и их повторений
for k in list_words:     # цикл перебора слов
    dict_words[k] = list_words.count(k)
print(dict_words)  # 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

list_words_unic = list(dict_words.items())
list_words_unic.sort(key=lambda i: i[1])
list_words_unic.reverse()
print(list_words_unic[:5])  # 4) вывести 5 наиболее часто встречающихся слов (sort)

set_words = set(dict_words.keys())
print(set_words)  # вывести количество разных слов в тексте (set)





