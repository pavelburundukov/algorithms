# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой, так и отличаться.

import random

SIZE = 20
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print("========================================================") 

# два наименьших элемента
min_items = [float("inf"), float("inf")]

for i in range(len(array)):
  # если это первый наименьший элемент
  if array[i] < min_items[0]:
    # сохраняем его
    min_items[0] = array[i]
    # и проверяем, нет ли ВТОРОГО наименьшего элемента ДО НЕГО
    for j in range(0,i):
      # если есть, то сохраняем и его
      if min_items[0] <= array[j] < min_items[1]:
        min_items[1] = array[j]
  # если это не первый наименьший элемент, проверяем является ли он вторым      
  elif min_items[0] <= array[i] < min_items[1]:
    min_items[1] = array[i]

print(min_items)
