number1 = int(input('Enter a number '))
list1 = [*range(1, number1+1)]
list2 = []
print(list1)

for item in list1:
    if number1 % item == 0:
        list2.append(item)
if len(list2) != 0:
    print('Divisor for', number1,'=', list2)
else:
    print('There is no divisor')