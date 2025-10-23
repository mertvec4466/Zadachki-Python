import math
a=float(input('введите значение a: '))
b=float(input('введите значение b: '))
def ur(a,b):
    for x in range(-1000,1000):
        if a == 0:
            print('недопустимое значения a')
        if x in range(-1000,1000):
            abx=(a*x+b)
            if (int(abx) == 0):
                return(x)
            elif x not in range(-1000,999):
                return ('нет решений')
print(ur(a,b))