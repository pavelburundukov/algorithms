# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# находим индексы минимального и максимального элемента
min_item = float("inf")
max_item = float("-inf")

for i in range(len(array)):
  if array[i] < min_item:
    min_item = array[i]
    min_idx = i
  if array[i] > max_item:
    max_item = array[i]
    max_idx = i 

# находим сумму элементов между этими индексами    
total = 0
for idx in range(min_idx+1, max_idx):
  total += array[idx]

print(total)
