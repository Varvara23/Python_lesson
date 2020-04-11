# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000./
# Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)

def one(x):
    for k in range(2,x):
        if x%k == 0:
            # print(k)
            return 0
    return 1

# 2) выводит список всех делителей числа

def two(x):
    for k in range(1,x+1):
        if x%k == 0:
            print(k)

# 3) выводит самый большой простой делитель числа

def three(x):
    max = 1
    for k in range(1,x+1):
        if x%k == 0:
            if one(k) == 1:
                max = k
    print(max)

# 4) функция выводит каноническое разложение числа на простые множители
def four(x):
    list_num = []
    k = 2
    while k*k<=x:
        while x%k == 0:
            x = x/k
            list_num.append(k)
        k = k + 1
    if x>1:
        list_num.append(int(x))
    return print(list_num)


# 5) функция выводит самый большой делитель (не обязательно простой) числа
# Кроме самого исходного числа
def five(x):
    max = 1
    for k in range(1,x):
        if x%k == 0:
            max = k
    print(max)