# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input("Enter a number: "))

a = x // 100
b = x % 100 // 10
c = x % 10
print("The sum is " + str(a+b+c))
print("The multiplication is " + str(a*b*c))

s = 0
m = 1
for i in str(x):
  s += int(i)
  m *= int(i)
print("The sum is " + str(s))
print("The multiplication is " + str(m))

input()
