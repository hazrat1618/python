password = input('Please type a password to check if it meets requirements:')

if len(password) >= 8 and '@' in password and ' ' not in password:
    print('Strong password')
else:
    print('Weak password')