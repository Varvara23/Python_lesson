import lesson_5_module

n = int(input("Введите число: "))
if lesson_5_module.one(n) == 1:
    print('Число простое')
else:
    print('Число не простое')

print('Делители числа: ')
lesson_5_module.two(n)

print('Максимально простой делитель: ')
lesson_5_module.three(n)