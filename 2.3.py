# Sector A
import math

a=float(input('input a: '))
Pa=math.sin(math.fabs(3*a))
Pb=math.sqrt((2*a+Pa)/3.56)
print(Pb)



# Sector B
x=float(input('input x: '))
print(math.sin((3.2+math.sqrt(1+x))/math.fabs(5*x)))