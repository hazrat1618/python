inp = input('Type a word: ')

new_dict = {}
for char in inp:
    if char in new_dict:
        new_dict[char] += 1
    else:
        new_dict[char] = 1

print(new_dict)