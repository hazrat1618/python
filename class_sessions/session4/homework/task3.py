inp = input('Type a list of numbers: ').split()

new_list = []
for char in inp:
    if char not in new_list:
        new_list.append(char)

print(new_list)