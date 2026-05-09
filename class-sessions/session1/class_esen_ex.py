try:
    result = int(input("enter age: "))
    print(result)
except ValueError:
    print("this is not valid number")
except Exception as e:
    print("print went wront: ", e)