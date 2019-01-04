# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# найти индексы минимального и максимального значений
min_item = float("inf")
max_item = float("-inf")

for i in range(len(array)):
  if array[i] < min_item:
    min_item = array[i]
    min_index = i
  if array[i] > max_item:
    max_item = array[i]
    max_index = i

# поменять местами эти значения
array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)
