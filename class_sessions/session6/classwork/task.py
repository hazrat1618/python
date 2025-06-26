students = {
    "bob": 80,
    "rob": 55,
    "jack": 75,
    "tobby": 95
}

# Function
# def score(students):
#     name = input("enter a student's name: ")
#     try:
#         return students[name]
#     except KeyError:
#         return f"{name} not found, enter existing user."
    
# print(score(students))

# or 2nd way

name = input("enter a student's name: ")

try:
    score = students[name]
    print(f"Student{name} got {score}")
except KeyError:
    print(f'Student {name}, doesnt exist')