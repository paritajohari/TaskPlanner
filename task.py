
class Task:

	valid_types = ["Feature", "Bug", "Story"]
	
	def __init__(self, title, creator, task_type, due_date, assignee = "", status = "Open"):
		self.title = title
		self.creator = creator
		self.assignee = assignee
		self.status = status
		self.due_date = due_date
		self.task_type = task_type
		
	def update_status(self, type, status):
		self.status = status
				
	def display_task(self):
		task = {"Title": self.title, "Creator": self.creator, "Assignee": self.assignee, "Status": self.status, "Type": self.task_type, "Due_date": self.due_date}
		print(task)
		
	def create_subtrack(self, task):
		if self.status != "Completed":
			self.subtrack.append(task)


class Feature(Task):
	valid_states = ["Open", "In progress", "Testing", "Deployed"]
	def __init__(self, *, title, creator, assignee = "", status = "Open", type, due_date, summary, impact):
		self.summary = summary		
		if TaskValidation.validateImpact(impact) == True:
			self.impact = impact
		else:
			print("Invalid input")
		#Task.__init__(self, * , title, creator, assignee, status, type, due_date)
			
			
class Bug(Task):
	valid_states = ["Open", "In progress", "Fixed"]
	def __init__(self, * , title, creator, assignee = "", status = "Open", type, due_date):
		for key, value in args:
			if key == "severity":
				if TaskValidation.validateSeverity(value) == True:
					self.severity = value
				else:
					print("Invalid input")
			else:
				print("Error missing parameter")
			
class Story(Task):
	valid_states = ["Open", "In progress", "Completed"]
	def __init__(self, **args):
		for key, value in args:
			if key == "summary":
				self.summary = value
			elif key == "subtrack":
				self.subtrack = value
			else:
				print("Error missing parameter")		


if __name__ == "__main__":
	task = Task(title = "First task", creator = "", assignee = "", status = "Open", type = "Bug", due_date = "12/19/2019")
	task.displayTask()