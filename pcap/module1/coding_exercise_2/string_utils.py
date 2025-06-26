def halve_string(input_string):
	mid = (len(input_string)+ 1) // 2
	return input_string[:mid], input_string[mid:]


	# •	Takes a single string (input_string) as a parameter.
	# •	Calculates the midpoint of the string.
	    # •	len(input_string) gives total characters.
	    # •	+1 // 2 ensures if the length is odd, the first half is longer.
	        # •	Example: 'abcde' → midpoint is 3 → ('abc', 'de')
	# •	Then we slice the string:
	    # •	input_string[:mid] gets the first half.
	    # •	input_string[mid:] gets the second half.
