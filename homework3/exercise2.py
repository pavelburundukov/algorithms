# 2. Во втором массиве сохранить индексы чётных элементов первого массива.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# создать и заполнить новый лист индексами чётных элементов 
out = list()
for i in range(len(array)):
  if array[i] % 2 == 0:
    out.append(i)

print(out)



