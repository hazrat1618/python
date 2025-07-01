# need to import sys module using import sys cmd
# names are: sys.stdin, sys.stdout, sys.stderr

import sys  # Import sys module to access system-related functions like stdin

# Loop through each line entered by the user via standard input (keyboard)
for line in sys.stdin:
    # Remove any trailing newline or spaces from the input
    if line.rstrip() == 'q':  
        break  # Exit the loop if the user types 'q'
    
    print(line)  # Otherwise, print the line the user typed

# After exiting the loop, print a goodbye message
print('You pressed q, so I want to quit now. Bye!')