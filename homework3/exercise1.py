# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел от 2 до 9.

array = list(range(2,100))
digits = list(range(2,10))

# вложенный цикл чтобы пройти по всем натуральным числам для каждой цифры
out = [0, 0, 0, 0, 0, 0, 0, 0]
for digit in digits:
  for item in array:
    if item % digit == 0:
      out[digit-2] += 1

print(out)
    
  


