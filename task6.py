str1 = input("Enter a word: ")
list1 = list(str1)
list2 = list1[::-1]
list3 = []

if list1 == list2:
    print('polindrome')
else:
    print('not polindrome')

for item in list2:
    list3.append(item)
print(list3)