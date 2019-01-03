# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через # эти точки.

print("Координаты точки A - (x1, y1):")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

print("Координаты точки B - (x2, y2):")
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print("Уравнение прямой, проходящей через точки A и B:")
if x1 == x2:
  print("x = " + str(x1))
else:
  k = (y1 - y2) / (x1 - x2)
  b = y2 - k*x2
  print("y = " + str(k) + " * x + " + str(b))
