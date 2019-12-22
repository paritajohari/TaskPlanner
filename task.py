
class Task:

	valid_types = ["Feature", "Bug", "Story"]
	task_id = 0
	
	def __init__(self, title, creator, task_type, due_date, assignee = "", status = "Open", sprint_id = ""):
		Task.task_id += 1
		self.id = Task.task_id
		self.title = title
		self.creator = creator
		self.assignee = assignee
		self.status = status
		self.due_date = due_date
		self.task_type = task_type
		self.sprint_id = sprint_id
	
	def update_assignee(self, assignee):
		self.assignee = assignee
	
	def update_sprint(self, sprint_id):
		self.sprint_id = sprint_id
		
		
	def display_task(self):
		task = {"Title": self.title, "Creator": self.creator, "Assignee": self.assignee, "Status": self.status, "Type": self.task_type, "Due_date": self.due_date}
		print(self.__dict__)


class Feature(Task):
	valid_states = ["Open", "In progress", "Testing", "Deployed"]
	valid_impacts = ["Low", "Moderate", "High"]
	
	def __init__(self, title, creator, task_type, due_date, summary, impact, assignee = "", status = "Open", sprint_id = ""):
		Task.__init__(self, title, creator, task_type, due_date, assignee, status, sprint_id)
		self.summary = summary		
		self.impact = impact
	
	def update_status(self, status):
		if status in Feature.valid_states:
			self.status = status
		else:
			print("Invalid status for a Feature")
		
	'''def display_task(self):
		task = {"Title": self.title, "Creator": self.creator, "Assignee": self.assignee, "Status": self.status, "Type": self.task_type, "Due_date": self.due_date, "Summary": self.summary, "Impact": self.impact}
		print(self.__dict__)'''
			
			
class Bug(Task):
	valid_states = ["Open", "In progress", "Fixed"]
	valid_severities = ["P0", "P1", "P2"]
	
	def __init__(self, title, creator, task_type, due_date, severity, assignee = "", status = "Open", sprint_id = ""):
		Task.__init__(self, title, creator, task_type, due_date, assignee, status, sprint_id)
		self.severity = severity
	
	def update_status(self, status):
		if status in Bug.valid_states:
			self.status = status
		else:
			print("Invalid status for a Bug")
		
			
class Story(Task):
	valid_states = ["Open", "In progress", "Completed"]	
	
	def __init__(self, title, creator, task_type, due_date, summary, assignee = "", status = "Open", sprint_id = ""):
		Task.__init__(self, title, creator, task_type, due_date, assignee, status, sprint_id)
		self.summary = summary
		self.subtrack = {}
		self.subtrack_count = 0
	
	def add_subtrack(self, subtrack):
		if self.status != "Completed":
			self.subtrack_count += 1
			self.subtrack[self.subtrack_count] = subtrack
	
	def update_status(self, status):
		if status in Story.valid_states:
			self.status = status
		else:
			print("Invalid status for a Story")

class SubTrack():
	valid_states = ["Open", "In progress", "Completed"]	
	
	def __init__(self, title, status):
		self.title = title
		self.status = status


	def update_status(self, status):
		if status in SubTrack.valid_states:
			self.status = status
		else:
			print("Invalid status for a SubTrack")

		
if __name__ == "__main__":
	task = Task(title = "First task", creator = "", assignee = "", status = "Open", type = "Bug", due_date = "12/19/2019")
	task.displayTask()