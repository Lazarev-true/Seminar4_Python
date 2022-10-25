# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от -100 до 100) многочлена и 
# записать в файл многочлен степени k k - максимальная степень 
# многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 
# просто пропускаем данную итерацию степени

import random

def get_sub(y):
    translation = y.maketrans({"2": "\u00B2", "3": "\u00B3", "4": "\u2074", 
                                "5": "\u2075", "6": "\u2076", "7": "\u2077", 
                                "8": "\u2078", "9": "\u2079", "0": "\u2070", "1": "\u00B9"})
    return y.translate(translation)

k = int(input('Введите максимальную степень k (от 1 до ..) '))

if k < 1:
    print('Степень не должна быть меньше единицы')
    exit()
else:
    m = random.randint(1, k)
    degree = random.sample(range(k), m)
    degree.sort()

    S = ''
    sign = ''

    for i in reversed(degree):
        x = random.randint(-1, 3)
        print(x)
        p = 'x'
        I = str(i)

        if x < 0:
            x = abs(x)
            sign = '-'
        else:
            sign = '+'

        if x == 0:
            continue
        elif x == 1 and i == 0:
            x = 1
        elif x == -1 and i == 0:
            x = -1
        elif x == 1 or x == -1:
            x = ''
        
        if i == 1:
            I = ''
        if i == 0:
            p = ''
            I = ''
            
        S += f'{sign}{x}{p}{get_sub(I)}'

    if k == 1:
        S += '!'

    S += '=0'

    if S[0] == '+':
        S = S[1:]

    file = open("Task4", "w", encoding='utf-8')
    file.write(str(S))
    file.close()

    print(S)
