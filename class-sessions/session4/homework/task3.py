inp = input("type a list of number: ").split()

new_list = []

for char in inp:
    num = int(char)
    if num not in new_list:
        new_list.append(num)

print(new_list)