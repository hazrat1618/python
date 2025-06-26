# File with our custom module
# Each module is initialized once
# __name__ == module2
# __name__ == module1
# name__ == __main__

# module2.py: print('Hello') --> module1.py: import module2 --> main.py: import module1, import module2
# if we run python main.py, print('Hello') will be shown once
if __name__ == '__main__':
    print('File executed directly')
else:
    print('File executed as a module')

# If we start variable name with one or two underscores(_), it means the users of module
#should never modify the variable. ex: _my_var, __my_var

#(.venv) [root@python 17_modules_own_modules]# python main.py 
#File executed as a module
#(.venv) [root@python 17_modules_own_modules]# python own_module_17.py 
#File executed directly
#(.venv) [root@python 17_modules_own_modules]# 

