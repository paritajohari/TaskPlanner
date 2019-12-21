from task_validator import Validator
from task import Task, Feature, Bug, Story, SubTrack
import utils

class TaskPlanner:
	# class variable
	default_status = "open"
	
	def create_task(self):
		title = utils.read_input("Title: ", Validator.stringvalidator)
		creator = utils.read_input("Creator: ", Validator.stringvalidator)
		assignee = input("Assignee: ")
		task_type = utils.read_input("Type: ", Validator.typevalidator)
		due_date = utils.read_input("Due-Date: ", Validator.datevalidator)

		if task_type == "Feature":
			summary = utils.read_input("Summary: ", Validator.stringvalidator)
			impact = utils.read_input("Impact: ", Validator.impactvalidator)
			return Feature(title, creator, task_type, due_date, summary, impact, assignee, TaskPlanner.default_status)
		elif task_type == "Bug":
			severity = utils.read_input("Severity: ", Validator.severityvalidator)
			return Bug(title, creator, task_type, due_date, severity, assignee, TaskPlanner.default_status)
		elif task_type == "Story":
			summary = utils.read_input("Summary: ", Validator.stringvalidator)
			story = Story(title, creator, task_type, due_date, summary, assignee, TaskPlanner.default_status)
			if input("Do you want to create sub-track? Type y or n: ") == "y":
				self.create_subtrack(story)
			return story
				

	def create_subtrack(self, story_obj):
		sub_title = utils.read_input("Sub-track Title: ", Validator.stringvalidator)
		s = SubTrack(sub_title, TaskPlanner.default_status)
		story_obj.add_subtrack(s)
		
	
	def start(self):
		TaskPlanner.show_menu()
		choice = input("Choice: ")
		while(choice != "X"):
			if choice == "1":
				task = self.create_task()
				task.display_task()
				
			TaskPlanner.show_menu()
			choice = input("Choice: ")
		
		
	def show_menu():
		print('''
1. Create Task
2. Create SubTrack
3. Change Status
4. Change Assignee
5. Display user specific tasks
X. Exit
		''')
			
	
		
		
if __name__ == "__main__":
	tp = TaskPlanner()
	'''newtask = tp.create_task()
	newtask.display_task()
	tp.create_subtrack(newtask)
	newtask.display_task()'''
	tp.start()
	
	
		
		
	