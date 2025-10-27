import math

a=float(input('введите катет a: '))
b=float(input('введите катет b: '))
c=math.sqrt(abs(a**2+b**2))
p=(a+b+c)
print('периметр прямоугольного треугольника равен',p)