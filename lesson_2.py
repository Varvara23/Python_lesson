# Задачи на циклы и оператор условия

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# for i in range(1,6,1):
#        print(i," ",0)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# count = 0
# for i in range(0,10,1):
#        n = int(input("Введите цифру: "))
#        if n == 5:
#               count += 1
# print("Всего цифр 5: ", count)


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum += i
# print(sum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

# s = 1
# for i in range(1,11):
#     s *= i
# print(s)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# int_num = 2129
# while int_num>0:
#     print(int_num%10)
#     int_num = int_num//10

'''
Задача 6
Найти сумму цифр числа.
'''
# n = int(input("Введите число: "))
# sum = 0
# while n>0:
#        d = n%10
#        n = n//10
#        sum += d
# print('сумма всех цифр этого числа=', sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# n = input('Введите число: ')
# count = 1
# for i in n:
#     count *= int(i)
# print(count)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# int_num = 213413
# while int_num>0:
#     if int_num%10 == 5:
#         print('Yes')
#         break
#     int_num = int_num//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# n = int(input('Введите число:'))
# m = -1
# while n>0:
#        d = n%10
#        if d>m:
#               m = d
#        n = n//10
# print(m)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# n = int(input("Введите число: "))
# count = 0
# while n>0:
#        d = n%10
#        n = n//10
#        if d == 5:
#               count += 1
# print("Всего цифр 5: ", count)
