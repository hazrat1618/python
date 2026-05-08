dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"banana": 2, "orange": 4, "grape": 6}

for key,value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value

print(dict1)