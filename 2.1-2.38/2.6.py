import math

h=float(input('Задайте точку высоты: '))
r=6350
formula= math.sqrt(abs((r + h) ** 2 - r ** 2))
print(f"Расстояние до линии горизонта при высоте {h}км: {formula:.2f}км")