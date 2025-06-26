# at start we did python <this file name> and python detected that the file is imported as a module and tests were skipped
import list_utils

my_list = [23, 21, 2, 5, 72]

print(list_utils.sum_elements(my_list))

# We get output 123 cause it used imported func from list_utils.py