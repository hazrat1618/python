number = int(input('Please inter a number: '))

if number > 0 and number % 2 == 0:
    print('The number is positive')
    print('The number is even')
elif number > 0 and number % 2 == 1:
    print('The number is positive')
    print('The number is odd')
elif number < 0 and number % 2 == 0:
    print('The number is negative')
    print('The number is even')
elif number < 0 and number % 2 == 1:
    print('The number is negative')
    print('The number is odd')
elif number == 0: 
    print('Number is 0')
else:
    print('Please enter valid number')

