#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше #другого).

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if y < x < z or z < x < y:
  print("the first number is between the second and the third")
elif x < y < z or z < y < x:
  print("the second number is between the first and the third")
else:
  print("the third number is between the first and the second")
