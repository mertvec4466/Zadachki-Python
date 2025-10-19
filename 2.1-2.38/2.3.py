# Sector A
import math

a=float(input('input a: '))
Pa=math.sin(abs(3*a))
pd= 2*a+Pa
Pb=math.sqrt(abs(pd) / 3.56)
print(Pb)



# Sector B
x=float(input('input x: '))
print(math.sin((3.2+math.sqrt(abs(1+x))/(5*x))))