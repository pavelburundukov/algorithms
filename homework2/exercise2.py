#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число #34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

x = int(input("Введите натуральное число: "))

a = 0 # чётные цифры 
b = 0 # нечётные цифры
for i in str(x):
  if int(i) % 2 == 0:
    a += 1
  else:
    b += 1
    
print("В числе " + str(a) + " чётных чисел и " + str(b) + " нечётных чисел")
    
    
  