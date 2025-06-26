# Session 5

# Dictionaries 
# Sets 

# Functions

# Dictionary is the data type that can hold multiple key value pairs

# Mutable - list, dict
# Immutable - str, tpl, int, float, bool ...

laptop = {
    "Dell": {
        "software": {
            "os": "linux mint",
            "version": "22.04",
            "applications": ["python", "vscode", "slack"]
        },

        "hardware": {
            "cpu": "Intel Core i5, (6 cores)",
            "ram": "8gb",
            "storage": "256gb",
            "screen": "ips"
        }
    },
    
    "MacBook": {
        "software": {
            "os": "Mac OS",
            "version": "Sequoia 15.01",
            "applications": ["telegram", "slack", "ms teams"]
        },

        "hardware": {
            "model": "macbook pro",
            "cpu": "M1 pro",
            "ram": "16 gb",
            "storage": "1024 gb",
            "screen": "ips"
        }
    },

    "Acer": {
        "software": {
            "os": "Linux Ubuntu",
            "version": "22.04",
            "applications": ["python", "nodejs", "slack"]
        },

        "hardware": {
            "model": "Swift 16",
            "cpu": "Inter Core i9, (16 cores)",
            "ram": "32gb",
            "storage": "1tb",
            "screen": "oled"
        }
    }
}

# Task1
# new_list = []
# for key, value in laptop.items():
#     print(key)

# Task2
# for key,value in laptop.items():
#     print(f"Laptop model is : {key}")
#     print(OS is: ", value["software"]["os"])
#     print(f"Version: {value['software']['version']}")

# Task3
# for key,values in laptop.items():
#     print(f"Laptop model is : {key}")
#     print(f"Application: ", end = "")

#     for element in values['software']['applications']:
#         print(element, end=' ')
#     print()


# fruits = {"banana": 2, "apple": 1, "pear": 3}
# fruits["cherry"] = 4
# fruits['pineapple']= 7

# fruits.pop("apple")

# del fruits['pear']
# print(fruits)


# sets - mutable
# stores only unique values

# List preserve orser and allow duplicate
# Sets remove duplicate and do not preserve order

# 1st example:
# lst = [1, 1, 1, 1, 1]
# print(lst)


# sets = {1, 1, 1, 1, 1}
# print(sets)

# 2nd example:
# lst = [10, 1, -1, 1, 1]
# print(lst)


# sets = {10, 1, -10, -1, 1, 1, 9, 11, 12}
# print(sets)


# Functions
# A function is a block of reusable code designed to perform a specific task
# Helps in organizing code, making it readable, modular, and reusable

# What is return --> python keyword that is used only in functions
# return is used to output a data type

# 1 ex
# def greet(name):
#     print(f"Hello, {name}")

# inp = input("What is your name? ")
# greet(inp)

# 2nd ex. We get NoneType. It is recommended to use return instead of print with func
# def add(num1, num2):
#     print(num1 + num2)

# sum = add(5, 10) 
# print(type(sum))

# 3rd ex using return:
# def add(num1, num2):
#     return(num1 + num2)

# sum = add(5, 10) 
# print(type(sum))