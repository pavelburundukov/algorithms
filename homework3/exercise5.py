# 5. В массиве найти максимальный отрицательный элемент. Вывести его значение и позицию в массиве.

import random

SIZE = 50
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print("========================================================") 

min_item = float("inf")
min_idx = None
for i in range(len(array)):
  if array[i] >= 0:
    continue
  if array[i] < min_item:
    min_item = array[i]
    min_idx = i
    
print(min_item, min_idx) 
