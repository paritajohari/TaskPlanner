# global functions
def read_input(msg, func):
	value = input(msg)
	
	while(not func(value)):
		print("Invalid input. Please try again")
		value = input(msg)
	
	return value

# normal variable/functions (outside class)
	# access directly using name
# class variable/functions (inside class but outside functions and functions_without_self_parameter)
	# access using class name
# instance variable/functions (inside __init__ or being accessed using self)
	# access using object-name/self