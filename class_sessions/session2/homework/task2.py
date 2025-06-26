first_boolean = input('Please type first boolean: ')
second_boolean = input('Please type second boolean: ')

if first_boolean == 'True' and second_boolean == 'True':
    print( '''
        True and True = True
        True or True = True
          ''')
elif first_boolean == 'True' and second_boolean == 'False' or first_boolean == 'False' and second_boolean == 'True':
    print( '''
        True and False = False
        True or False = True
          ''')
elif first_boolean == 'True' and second_boolean == '' or first_boolean == '' and second_boolean == 'True':
    print('not True = Fasle')
elif first_boolean == 'False' and second_boolean == '' or first_boolean == '' and second_boolean == 'False':
    print('not False = True')
else:
    print('Please type a valid form of boolean.')
