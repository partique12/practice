elements1 = [3, 5, 8, 13, 21, 34, 55, 89]
elements2 = []
elements3 = []
for element in elements1:
    if element<5:
        elements2.append(element)
#print(elements2)


number1 = int(input('Enter a number '))
for element in elements1:
    if element < number1:
        elements3.append(element)          
if len(elements3)==0:
    print('No numbers smaller than entered')
else:
    print (elements3)
print('Good luck')