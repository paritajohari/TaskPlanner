from task_validator import Validator
from task import Task, Feature, Bug, Story, SubTrack
import utils

class TaskPlanner:
	# class variable
	default_status = "open"

	def __init__(self):
		self.all_tasks = {"feature": {}, "bug": {}, "story": {}}
	
	def create_task(self):
		title = utils.read_input("Title: ", Validator.stringvalidator)
		creator = utils.read_input("Creator: ", Validator.stringvalidator)
		assignee = input("Assignee: ")
		task_type = utils.read_input("Type: ", Validator.typevalidator)
		due_date = utils.read_input("Due-Date: ", Validator.datevalidator)

		if task_type == "Feature":
			summary = utils.read_input("Summary: ", Validator.stringvalidator)
			impact = utils.read_input("Impact: ", Validator.impactvalidator)
			feature = Feature(title, creator, task_type, due_date, summary, impact, assignee, TaskPlanner.default_status)
			self.all_tasks["feature"][feature.id] = feature
		elif task_type == "Bug":
			severity = utils.read_input("Severity: ", Validator.severityvalidator)
			bug = Bug(title, creator, task_type, due_date, severity, assignee, TaskPlanner.default_status)
			self.all_tasks["bug"][bug.id] = bug
		elif task_type == "Story":
			summary = utils.read_input("Summary: ", Validator.stringvalidator)
			story = Story(title, creator, task_type, due_date, summary, assignee, TaskPlanner.default_status)
			if input("Do you want to create sub-track? Type y or n: ") == "y":
				self.create_subtrack(story)
			self.all_tasks["story"][story.id] = story
				

	def create_subtrack(self, story_obj):
		sub_title = utils.read_input("Sub-track Title: ", Validator.stringvalidator)
		s = SubTrack(sub_title, TaskPlanner.default_status)
		story_obj.add_subtrack(s)


	def start(self):
		TaskPlanner.show_menu()
		choice = input("Choice: ")
		while(choice != "X"):
			if choice == "1":
				self.create_task()
			elif choice == "2":
				self.show_stories()
				story_id = int(input("Select story ID to add sub-track to: "))
				story_obj = self.all_tasks["story"].get(story_id, None)
				if story_obj:
					self.create_subtrack(story_obj)
				else:
					print("Invalid story selection. Please try again.")
			elif choice == "3":
				self.show_tasks()
				task_id = int(input("Select task ID for status change: "))
				task_obj = self.get_task(task_id)
				if task_obj:
					if task_obj.task_type == "Story":
						status_choice = input("Do you want to change status of story(1) or sub-track(2): ")
						if status_choice == "2":
							self.show_subtracks(task_obj)
							subtrack_id = int(input("Select subtrack ID for status change: "))
							subtrack_obj = task_obj.subtrack.get(subtrack_id, None)
							if subtrack_obj:
								new_status = input("Enter new status for sub-track: ")
								subtrack_obj.update_status(new_status)
							else:
								print("Invalid sub-track selection. Please try again.")
						else:
							new_status = input("Enter new status for selected task: ")
							task_obj.update_status(new_status)
					else:
						new_status = input("Enter new status for selected task: ")
						task_obj.update_status(new_status)
				else:
					print("Invalid task selection. Please try again.")
			elif choice == "4":
				self.show_tasks()
				task_id = int(input("Select task ID for status change: "))
				task_obj = self.get_task(task_id)
				if task_obj:
					assignee = input("New assignee: ")
					task_obj.update_assignee(assignee)
				else:
					print("Invalid task selection. Please try again.")
			elif choice == "5":
				assignee = input("Assignee: ")
				self.list_tasks_by_assignee(assignee)
			
			TaskPlanner.show_menu()
			choice = input("Choice: ")

	def list_tasks_by_assignee(self, assignee):
		for task_type, tasks in self.all_tasks.items():
			print("Task type: " + task_type)
			for task in tasks.values():
				if task.assignee == assignee:
					print("\tTitle: " + task.title)
					print("\tSprint: ")
				if task.task_type == "Story":
					print("\tSub-track:")
					for subtrack in task.subtrack.values():
						print("\t\t", subtrack.title)
	

	def show_subtracks(self, story):
		print("SUB_TRACK_ID\t|\tTITLE")
		for id, st in story.subtrack.items():
			print(id, "\t|\t", st.title)


	def get_task(self, id):
		for task_type, tasks in self.all_tasks.items():
			if id in tasks:
				return tasks[id]
		return None
	
	
	def show_tasks(self):
		print("TASK_ID\t|\tTYPE\t|\tTITLE")
		for task_type, tasks in self.all_tasks.items():
			for task in tasks.values():
				print(str(task.id) + "\t|\t" + task.task_type + "\t|\t" + task.title)


	def show_stories(self):
		print("STORY_ID\t|\tTITLE")
		for story in self.all_tasks["story"].values():
			print(str(story.id) + "\t\t|\t" + story.title)


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
	
	
		
		
	