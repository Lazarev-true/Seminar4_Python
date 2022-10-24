# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f1 = open('Task5_1', 'r')
f2 = open('Task5_2', 'r')

def get_sub(y):
    translation = y.maketrans({"2": "\u00B2", "3": "\u00B3", "4": "\u2074", 
                                "5": "\u2075", "6": "\u2076", "7": "\u2077", 
                                "8": "\u2078", "9": "\u2079", "0": "\u2070", "1": "\u00B9"})
    return y.translate(translation)

def simplification(f):
    s = f.read().replace('- ','+-')
    lst = s.replace('x',' x ')
    lst = lst.replace('^', '')
    lst = lst.replace('= 0', '')
    lst = lst.split('+')
    lst = [i.split() for i in lst]
    for i in lst:
        if i[0] == 'x': i.insert(0, '1')
        if i[-1] == 'x': i.append('1')
        if len(i) == 1: i.append('0')
    for i in lst:
        if i[1] == 'x':
            i.remove('x')
    for i in lst:
        i[0] = int(i[0])
        i[-1] = int(i[-1])
    return lst

lst1 = simplification(f1)
lst2 = simplification(f2)

def dictionary(lst):
    list(map(tuple, lst))
    leaders, key = zip(*lst)
    myDict = {key[i]: int(leaders[i]) for i in range(0, len(key), 1)}
    return myDict

myDict1 = dictionary(lst1)
myDict2 = dictionary(lst2)

d = myDict1
for key, value in myDict2.items():
    if key in myDict1:
        d[key] += value
    else:
        d.update({key: value})

lst = sorted(d.items(), key = lambda x: x[0])

S = ''

for i in reversed(lst):
    x = i[1]
    p = 'x'
    I = str(i[0])

    if x == 0:
        continue
    elif x == 1 or x == -1:
        x = ''
    elif x < 0:
        x = abs(x)
        token = ' - '
    else:
        token = ' + '
    
    if i[0] == 1:
        I = str()
    if i[0] == 0:
        p = ''
        I = str()
            
    S += f'{token}{x}{p}{get_sub(I)}'

if S == '':
    S += '0'

S += ' = 0'

if S[1] == '+':
        S = S[3:]

file = open("Task5_Sum", "w", encoding='utf-8')
file.write(str(S))
file.close()

print(S)   
