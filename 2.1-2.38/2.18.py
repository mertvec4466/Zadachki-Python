import math

x=float(input('введите значение x: '))
y=float(input('введите значение y: '))
z=(x+(2+y)/x**2) / y + (1 / math.sqrt(x**2+10))
q= 7.25 * math.sin(abs(x)) - abs(y)
print('z='+str(z))
print('q='+str(q))