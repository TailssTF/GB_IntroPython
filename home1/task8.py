# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите размер шоколадки и количество долек')
n = int(input())
m = int(input())
k = int(input())

if n * m - n == k or n * m - m == k:
    print('yes')
else:
    print('no')