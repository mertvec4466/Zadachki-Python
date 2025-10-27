import math

A=float(input('введите значение основания A: '))
B=float(input('введите значение основания B: '))
H=float(input('введите значение высоты: '))

delta=(abs(A-B))/2
c=(math.sqrt(abs(H**2+delta**2)))
P=A+B+(2*c)
print('Периметр равен:',P)
