import string_utils

def halve_strings(string_list):
    return [string_utils.halve_string(s) for s in string_list]

# •	It takes string_list as input — a list of strings.
# 	•	We use list comprehension to apply halve_string() to each string s.
    # 	•	This returns a list of tuples (one tuple per string), as expected.

# 2nd way
# import string_utils

# def halve_strings(string_list):
#     to_return = []
#     for string in string_list:
#         to_return.append(string_utils.halve_string(string))
#     return to_return