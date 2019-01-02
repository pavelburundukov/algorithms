#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся #пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. #Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не #'0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о #невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
  x = float(input("Enter the first number: "))
  y = float(input("Enter the second number: "))
  operation = input("Enter operation ('+','-','*','/' or '0' to exit: ")
  while not (operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '0'):
    operation = input("Enter correct operation ('+','-','*','/' or '0' to exit: ")
  if operation == '0':
    print("Exiting...")
    break
  if operation == '+':
    print(str(x) + " + " + str(y) + " = " + str(x + y))
  elif operation == '-':
    print(str(x) + " - " + str(y) + " = " + str(x - y))
  elif operation == '*':
    print(str(x) + " * " + str(y) + " = " + str(x * y))
  elif operation == '/':
    if y == 0:
      print("devision by 0 is not allowed!")
    else:
      print(str(x) + " / " + str(y) + " = " + str(x / y))

  
