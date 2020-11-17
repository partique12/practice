# user_input = input('Enter a number ')
# number1 = int(user_input)

# if number1 % 2 == 0 and number1 < 4:
#     print('Entered number is odd')
# elif number1 % 4 == 0:
#     print('Entered number is a multiple of 4')
# else:
#     print('Entered number is even')
# print('Well done!')

user_input2 = input('Enter one more number ')
number2 = int(user_input2)
user_input3 = input('..and another ')
number3 = int(user_input3)
if number2 % number3 == 0:
    print(number2, 'divides evently into', number3)
else:
    print(number2, 'is not divides evently into', number3)