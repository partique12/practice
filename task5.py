# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# len_b = len(b)
import random
a = random.sample(range(100), 10)
b = random.sample(range(100), 10)
print(a)
print(b)

for item in a:
     for item2 in b:
         if item == item2:
             c.append(item)
             c.append(item2)
mylist = list(dict.fromkeys(c))
print(mylist)