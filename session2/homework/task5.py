first = int(input('Type the side: '))
second = int(input('Type the side: '))
third = int(input('Type the side: '))

if first == second == third:
    print('Equilateral triangle')
elif first == second or first == third or second == third:
    print('Isosceles triangle')
elif (first + second <= third) or (first + third <= second) or (second + third <= first):
    print('Not a triangle')
else:
    print('Scalene')