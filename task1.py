"""
Считайте обезьян!
ОПИСАНИЕ:
Вы ведете своего сына в лес, чтобы увидеть обезьян.
Вы знаете, что там есть определенное число (n),
но ваш сын слишком мал, чтобы просто оценить полное число,
ему приходится начинать считать их с 1.

Как хороший родитель, вы будете сидеть и считать с ним.
Учитывая число (n), заполните массив всеми числами
до этого числа включительно, но исключая ноль.

Например (ввод --> вывод):
10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 1 --> [1]
"""

#Мое решение
def monkey_count(n):
    i = 1
    monkey_count = []
    while i<=n:
        monkey_count.append(i)
        i+=1
    return monkey_count

#Чужое решение
def monkey_count_1(n):
    return range(1, n+1)

def monkey_count_2(n):
    return list(range(1,n+1))

def monkey_count_3(n):
    return [i+1 for i in range(n)]


print(monkey_count(5))
print(monkey_count_1(5))
print(monkey_count_2(5))
print(monkey_count_3(5))