# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input("Введите кол-во чисел: "))
target = int(input("Введите цифру для поиска: "))

s = 0
for i in range(0,n):
  x = int(input("Введите число: "))
  for j in str(x):
    if j == str(target):
      s += 1
print("Цифра " + str(target) + " встречается " + str(s) + " раз.")
      