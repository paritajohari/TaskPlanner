def read_input(msg, func):
	value = input(msg)
	
	while(not func(value)):
		print("Invalid input. Please try again")
		value = input(msg)
	
	return value