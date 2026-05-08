inp_list = input('Please type words separated by space: ').split()

new_list = []
for val in inp_list:
    if val not in new_list:
        new_list.append(val)
print(new_list)
    