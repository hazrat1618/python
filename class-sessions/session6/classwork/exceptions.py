try:
    num = int(input('Enter a number: '))
    print(10 / num)
except ZeroDivisionError:
    print('Division by 0, not allowed')
except:
    print("Enter an integer value")
