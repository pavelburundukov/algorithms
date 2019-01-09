# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# Вариант 1 - алгоритм «Решето Эратосфена»

# n - до какого числа просеивать простые числа
def sieve1(n=100):
  out = list(range(n))
  out[1] = 0
  for i in range(2,n):
    if out[i] != 0:
      j = i + i
      while j < n:
        out[j] = 0
        j += i
  out = [i for i in out if i != 0]
  return(out)
  
# 100 loops, best of 3: 17.6 usec per loop -- n = 100
# 100 loops, best of 3: 223 usec per loop -- n = 1,000

# приблизительно линейный алгоритм


# Вариант 2 - прямолинейная проверка каждого из чисел

# n - до какого числа просеивать простые числа
def sieve2(n=100):
  not_prime = [] # НЕ простые числа
  for num in range(2,n):
    for div in range(2,num):
      if num % div == 0:
        not_prime.append(num)
  out = set(range(2,n)) - set(not_prime)
  return(out)
  
# 100 loops, best of 3: 339 usec per loop -- n = 100
# 100 loops, best of 3: 33.8 msec per loop -- n = 1,000

# намного-намного медленнее
          

# Тесты
def test(fun):
  prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
           47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
  out = fun() # равенство двух множеств
  assert(set(out) == prime)
  print("Test OK")

#test(sieve1)
#test(sieve2)

