# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

max_sum = 0
max_x = None

while True:
  x = int(input("Введите число: "))
  s = 0
  for i in str(x):
    s += int(i)
  if s > max_sum:
    max_x = x
    max_sum = s
  if x == 0:
    if max_x != None:
      print("Число " + str(max_x) + " имеет наибольшую сумму цифр, равную " + str(max_sum))
    print("Завершение работы...")
    break

