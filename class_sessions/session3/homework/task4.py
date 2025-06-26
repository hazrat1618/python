num_list = input('Type list of numbers: ').split()

second_highest = sorted(set(num_list))[-2]
print('Second highest numbers in list is: ',second_highest)