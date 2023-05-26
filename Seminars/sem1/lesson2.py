# циклы

# a = [1, 2, 3, 4]
# for element in a:
#    print(element)
#
# for i in range(len(a)):
#    print(a[i])



# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input('Введите N:'))
# i = 1
# result = 1
# if n == 0:
#     print(1)
# else:
#     while i <= n:
#         result *= i
#         i += 1
#
# print(result)

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# 0 1 1 2 3 5 8 13 21

# n = int(input('Введите N:'))
# i = 1
# a1 = 0
# a2 = 1
# flag = False
# while i <= n:
#     if a2 == n:
#         print(i+1)
#         flag = True
#         break
#     else:
#         temp = a2
#         a2 += a1
#         a1 = temp
#     i+=1
#
# if not flag:
#     print(-1)

# a1 = 0
# a2 = 1
# count = 2
# target = int(input('Введите натуральное число: '))
# if target <= 1:
#     print(target + 1)
# else:
#     while target > a2:
#         a2 = a1 + a2
#         a1 = a2 - a1
#         count += 1
#         print(a1, a2, count)
#
# if target == a2:
#     print(count)
# else:
#     print(-1)


# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input('Введите N:'))
min = float('inf')
max = 0
for i in range(n):
    a = int(input())
    if a < min:
        min = a
    if a > max:
        max = a
print(f'{min} {max}')

n = int(input('Введите N:'))
min = int(input())
max = min
for i in range(1, n):
    a = int(input())
    if a < min:
        min = a
    if a > max:
        max = a
print(f'{min} {max}')