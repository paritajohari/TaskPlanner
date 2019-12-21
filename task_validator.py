from dateutil.parser import parse
from task import Task, Feature, Bug

class Validator:
	
	# class functions
	def stringvalidator(str):		
		if str == "" or str == None:
			return False
		return True
		
		
	def typevalidator(task_type):
		if task_type in Task.valid_types:
			return True
		else:
			return False

			
	'''def statusvalidator(task_type, status):
		if type == "Feature" and status in :
			flag =  True
		elif type == "Bug" and status in :
			flag = True
		elif type == "Story" and status in :
			flag = True
		else:			
			flag = False
		return flag	'''
		
	def datevalidator(date):
		try:
			parse(date, fuzzy=False)
			return True
		except ValueError:
			return False
	
	def impactvalidator(impact):
		if impact in Feature.valid_impacts:
			return True
		else:
			return False
			
	def severityvalidator(severity):
		if severity in Bug.valid_severities:
			return True
		else:
			return False
			 
			 
if __name__ == "__main__":

	# Positive test case for string
	assert Validator.stringvalidator("This is test title") == True
	# Negative test case for string
	assert Validator.stringvalidator("") == False
	
	# Positive test case for status
	assert Validator.statusvalidator("Feature", "Open") == True
	# Negative test case for status
	assert Validator.statusvalidator("Bug", "blah") == False
	
	# Positive test case for date
	assert Validator.datevalidator("21/12/2019") == True
	# Negative test case for date
	assert Validator.datevalidator("blah") == False
	
	# Positive test case for impact
	assert Validator.impactvalidator("Low") == True
	# Negative test case for impact
	assert Validator.severityvalidator("blah") == False
	
	# Positive test case for severity
	assert Validator.severityvalidator("P0") == True
	# Negative test case for severity
	assert Validator.severityvalidator("blah") == False
	
	