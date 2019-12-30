class TaskError(Exception):


	def __init__(self, msg):
		self.msg = msg
		
		
	def print_msg(self):
		return ("Exception raised: ", self.msg)
	