# Решение для первого уровня
s = input("Введите пример с одним действием и двумя аршументами: ")
if '+' in s:
  a, b = s.split('+')
  print(int(a) + int(b))
elif '-' in s:
  a, b = s.split('-')
  print(int(a) - (b))
elif '*' in s:
  a, b = s.split('*')
  print(int(a) * int(b))
elif '/' in s:
  a, b = s.split('/')
  print(int(a) / int(b))




# Решение для второго уровня

import re
 
test_str = input("Введите пример с неограниченным количеством аргументов, но только с + или -: ")
res = sum(map(int, re.findall(r'[+-]?\d+', test_str)))
print("The evaluated result is : " + str(res))

# Решение для любых уровней

result = input("Введите любой пример: ")
print(eval(result))