with open("test.txt", "w") as file:
    file.write("hello devops")

with open("test.txt", "r") as file:
    data = file.read()
    print(data)