# Вычислить число Пи c заданной точностью d

from numpy import pi
import decimal
import math

D = decimal.Decimal

d1 = input('Задайте точность (напимер: 0.001) числа Пи: ')
j = len(d1)-2

d2 = float(d1) + 1

#j = 0
# while d1 != 1
#     j += 1
#     d1 *= 10

n = j

Pi_0 = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))
print(f'при d = {d1}, π = {D(str(Pi_0)).quantize(D(str(d2)), decimal.ROUND_FLOOR)}')

Pi_1 = (2 * math.acos( 0.0 ))
print(f'при d = {d1}, π = {round(Pi_1, j)}')

Pi_2 =  D(str(Pi_1)).quantize(D(str(d2)), decimal.ROUND_FLOOR)
print(f'при d = {d1}, π = {Pi_2}')

Pi_3 = math.ceil(math.pi)
print(f'π = {Pi_3}')

Pi_4 = pi
print(f'С точностью 3 знака, π = {"{:.3f}".format(Pi_4)}')
