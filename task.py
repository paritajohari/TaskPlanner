
class Task:

	valid_types = ["Feature", "Bug", "Story"]
	task_id = 0
	
	def __init__(self, title, creator, task_type, due_date, assignee = "", status = "Open"):
		Task.task_id += 1
		self.id = Task.task_id
		self.title = title
		self.creator = creator
		self.assignee = assignee
		self.status = status
		self.due_date = due_date
		self.task_type = task_type
	
	# instance functions
	def update_status(self, type, status):
		self.status = status
				
	def display_task(self):
		task = {"Title": self.title, "Creator": self.creator, "Assignee": self.assignee, "Status": self.status, "Type": self.task_type, "Due_date": self.due_date}
		print(self.__dict__)
		
	def create_subtrack(self, task):
		if self.status != "Completed":
			self.subtrack.append(task)


class Feature(Task):
	valid_states = ["Open", "In progress", "Testing", "Deployed"]
	valid_impacts = ["Low", "Moderate", "High"]
	
	def __init__(self, title, creator, task_type, due_date, summary, impact, assignee = "", status = "Open"):
		Task.__init__(self, title, creator, task_type, due_date, assignee, status)
		self.summary = summary		
		self.impact = impact
		
	'''def display_task(self):
		task = {"Title": self.title, "Creator": self.creator, "Assignee": self.assignee, "Status": self.status, "Type": self.task_type, "Due_date": self.due_date, "Summary": self.summary, "Impact": self.impact}
		print(self.__dict__)'''
			
			
class Bug(Task):
	# class variable
	valid_states = ["Open", "In progress", "Fixed"]
	valid_severities = ["P0", "P1", "P2"]
	def __init__(self, title, creator, task_type, due_date, severity, assignee = "", status = "Open"):
		Task.__init__(self, title, creator, task_type, due_date, assignee, status)
		# instance variable
		self.severity = severity
		
			
class Story(Task):
	valid_states = ["Open", "In progress", "Completed"]
	
	def __init__(self, title, creator, task_type, due_date, summary, assignee = "", status = "Open"):
		Task.__init__(self, title, creator, task_type, due_date, assignee, status)
		self.summary = summary
		self.subtrack = []
	
	def add_subtrack(self, subtrack):
		self.subtrack.append(subtrack)

class SubTrack():
	def __init__(self, title, status):
		self.title = title
		self.status = status
		
if __name__ == "__main__":
	task = Task(title = "First task", creator = "", assignee = "", status = "Open", type = "Bug", due_date = "12/19/2019")
	task.displayTask()