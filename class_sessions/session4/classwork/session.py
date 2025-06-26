# lst = [1, 2, 3]

# del lst[0]

# print(lst)

# True = 1
# False = 0
# lst = [2, 5, 1, -1, 0, -40.5]
# lst.sort()

# print(lst)

# lst = ["Hello", "Hello", "World"]
# print(lst.index("Hello"))

# str1 = "Hello World This is a test"

# lst_str = str1.split()
# print(lst_str)

# str1 = "Hello:World:This:is:a:test"

# lst_str = str1.split(':')
# print(lst_str)

# str1 = " Hello, World, This, is a test, "
# x = str1.split(',')
# filtered = []

# for word in x:
#     filtered.append(word.strip())

# print(filtered)

# lst_str = str1.split(',')
# print(lst_str)


# List comprehension
# [1, 2, .. 10]

# lst_num = []
# for num in range(1, 11):
#     if num % 2 == 0:
#         lst_num.append(num)

# print(lst_num)

# [[1,2], [1, 2], [1, 2].....total 10times.....[1, 2]]
# lst_num = [[1, 2] for num in range(10)]
# print(lst_num)

# table = [[i for i in range(1, 6)] for j in range(4)]
# print(table)

# Nested for loops

# for i in range(1, 8):
#     print(f"Run {i}")

#     for j in range(1, 6):
#         print(j, end=' ')

#     print()
#     print('-----------')

# Difference between mutable and immutable data types
# - Mutable ---> mutable -- change it's contents
# List —> append(), pop, change the order of the list, reverse the list, sort
# ex list:

# lst = ["Hello", "World", "Test"]

# lst[2] = "aKumo"

# print(lst)

# Immutable
# ex: str
# word = "Hell0"
# word[-1] = "o"

# print(word)


# Tuple   --> read only

# tpl = (1, 2, 3, 4)
# print(tpl)
# print(tpl[::-1])
# print(tpl)

# tpl = (1, "Hello", True, 50.3, ["Hello", "test", "World"])
# print(tpl[-1][1])

# print(sorted(tpl))

# index()
# does not change thetuple, but it gives the index where the value is located


# Dictionaries
# dict --> are the key value stores

# keys must be unique
# dictionaries = {"key": "value", "key2" : "value2"}
# print(dictionaries["key"])


# students = {
#     1:{"first_name": "John", "last_name": "Doe", "dob": "01/01/2000"},
#     2:{"first_name": "Alex", "last_name": "Poatan", "dob": "02/02/2000"},
#     3:{"first_name": "Steve", "last_name": "Robin", "dob": "01/03/2000"}
# }

# print(students[1]["first_name"])


# for key, value in students.items():
#     print(key, value)













