# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input("Введите натуральное число: "))

lhs = 0 # left hand side
for i in range(n+1):
  lhs += i
  
rhs = n*(n+1)/2 # right hand side

if lhs == rhs:
  print("Обе части равны.")
print("Левая часть: " + str(lhs))
print("Правая часть: " + str(rhs))
