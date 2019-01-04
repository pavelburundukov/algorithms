# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print("========================================================")

# словарь значений "число в массиве" - "сколько раз встречается"
out = dict() 
for item in array:
  if item in out:
    out[item] += 1
  else:
    out[item] = 1 
print(out)
    
# ключ максимального значения в словаре     
max_freq = float("-inf")
for key in out:
  if out[key] > max_freq:
    max_freq = out[key]
    max_item = key    
  
print("Наиболее часто встречаемое значение: " + str(max_item))
