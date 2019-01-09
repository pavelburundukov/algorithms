# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанного в рамках домашнего задания первых трёх уроков.

import random
import cProfile

# Задание: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Вариант 1 - классика:

def two_items1(array_size):
  array = [random.randint(-100, 100) for _ in range(array_size)]
  #print(array)
  # находим индексы минимального и максимального элементов
  idx_min = 0
  idx_max = 0
  for i in range(len(array)):
    if array[i] < array[idx_min]:
      idx_min = i
    elif array[i] > array[idx_max]:
      idx_max = i
  # меняем местами элементы 
  array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
  #print(array)  

# 100 loops, best of 3: 110 usec per loop -- array size 100
# 100 loops, best of 3: 1.11 msec per loop -- array size 1,000
# 100 loops, best of 3: 112 msec per loop -- array size 100,000


# Вариант 2 -  использование build-in functions:

def two_items2(array_size):
  array = [random.randint(-100, 100) for _ in range(array_size)]
  #print(array)
  min_item = min(array)
  max_item = max(array)
  idx_min = array.index(min_item)
  idx_max = array.index(max_item)
  array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
  #print(array) 
  
# 100 loops, best of 3: 105 usec per loop -- array size 100
# 100 loops, best of 3: 1.05 msec per loop -- array size 1,000
# 100 loops, best of 3: 104 msec per loop -- array size 100,000


# Выводы: 
# Скорость выполнения обоих вариантов растёт линейно с ростом размера массива.
# Второй вариант, хоть в теории и проходит по массиву 4 раза, на практике оказался немного быстрее. Причём, чем больше массив, тем второй вариант быстрее. 
# Это происходит из-за того, что встроенные функции min, max, array.index написаны на компилируемом языке низкого уровня C (python их лишь вызывает) и соответственно проход по массиву выполняется со скоростью C. 
# В то время как в первом варианте проход по массиву выполняется один раз, но зато выполняется интерпретатором python каждой строчки шаг за шагом.


#cProfile.run('two_items1(1000)')
#cProfile.run('two_items2(1000)')
# cProfile показал по одному вызову обоих функций - two_items1 и two_items2 

# Тесты
def test(fun):
  fun(10)
  fun(20)
  fun(30)

#test(two_items1)
#test(two_items2)


