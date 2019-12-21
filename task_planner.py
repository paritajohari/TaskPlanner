from task_validator import Validator
from task import Task
import utils

class TaskPlanner:
	default_status = "open"
	
	def createtask(self):
		title = utils.read_input("Title: ", Validator.stringvalidator)
		creator = utils.read_input("Creator: ", Validator.stringvalidator)
		assignee = input("Assignee: ")
		task_type = utils.read_input("Type: ", Validator.typevalidator)
		due_date = utils.read_input("Due-Date: ", Validator.datevalidator)
		t = Task(title, creator, task_type, due_date, assignee, TaskPlanner.default_status)
		return t


if __name__ == "__main__":
	tp = TaskPlanner()
	newtask = tp.createtask()
	newtask.display_task()
	
	
		
		
	