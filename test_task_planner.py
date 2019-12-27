from unittest import TestCase
from unittest import mock
from task_planner import TaskPlanner
import unittest
import task
import sys
import io


class TestTaskPlanner(TestCase):
	
	@mock.patch('builtins.input', create = True)
	def setUp(self, mocked_input):
		self.tp = TaskPlanner()
		self.tp.all_tasks = {"feature": {}, "bug": {}, "story": {}}
		lst = ["Title1", "Parita", "Kunal", "Feature", "25/12/2019", "Unit test case", "High"], ["Title2", "Parita", "Kunal", "Bug", "25/12/2019", "P0"], ["Title3", "Parita", "Kunal", "Story", "25/12/2019", "Unit test case", "y", "subtrack summary"]
		for l in lst:
			mocked_input.side_effect = l
			self.tp.create_task()
		self.tp.create_sprint("sp1")


	@mock.patch('builtins.input', create = True)
	def test_create_task(self, mocked_input):
		lst = ["Title4", "Parita", "Kunal", "Feature", "26/12/2019", "Unit test case", "High"], ["Title5", "Parita", "Kunal", "Bug", "26/12/2019", "P0"], ["Title6", "Parita", "Kunal", "Story", "26/12/2019", "Unit test case", "y", "subtrack summary1"]
		for l in lst:
			mocked_input.side_effect = l
			self.tp.create_task()
		count = 0
		for key, value in self.tp.all_tasks.items():
			for entry in value:
				count += 1
				
		self.assertEqual(count, 6)
		
		# Negative test
		# mocked_input.side_effect = ["Title1", "Parita", "Kunal", "Feature", "25dd/12/2019", "Unit test case", "High"]
		# self.assertRaises(Exception, self.tp.create_task())
				
	@mock.patch('builtins.input', create = True)
	def test_create_subtrack(self, mocked_input):
		for id, story in self.tp.all_tasks['story'].items():
			story_obj = story
		mocked_input.side_effect = ["Subtrack Title 1"]		
		self.tp.create_subtrack(story_obj)
		self.assertEqual(story_obj.subtrack_count, 2)
		
		
	def test_list_tasks_by_assignee(self):
		capturedOutput = io.StringIO()          # Create StringIO object
		sys.stdout = capturedOutput                   #  and redirect stdout.
		self.tp.list_tasks_by_assignee("Kunal")       # Call unchanged function.
		sys.stdout = sys.__stdout__                   # Reset redirect.		
		output = r'''Task type: feature
	Title: Title1
	Sprint:
Task type: story
	Title: Title3
	Sprint:
	Sub-track:
		subtrack summary
Task type: bug
	Title: Title2
	Sprint:
'''
		#print(capturedOutput.getvalue())
		#self.assertMultiLineEqual(output,a)

	
	def test_get_task(self):
		id = 11
		id = list(self.tp.all_tasks['feature'].keys())[0]
		self.assertNotEqual(self.tp.get_task(id),None)
	
	
	def test_create_sprint(self):
		id = "Sp2"
		self.tp.create_sprint(id)
		count = 0
		for key, value in self.tp.all_sprints.items():
			count += 1
		self.assertEqual(count, 2)
		

	def test_remove_sprint(self):
		id = list(self.tp.all_sprints.keys())[0]
		self.tp.remove_sprint(id)
		count = 0
		for key, value in self.tp.all_sprints.items():
			count += 1
		self.assertEqual(count, 0)
			
			
	def test_add_task_to_sprint(self):
		task_id = list(self.tp.all_tasks['feature'].keys())[0]
		id = list(self.tp.all_sprints.keys())[0]
		self.tp.add_task_to_sprint(id, task_id)
		count = 0
		for key, value in self.tp.all_sprints.items():
			for task in value:
				count += 1
		self.assertEqual(count, 1)
			

	def test_remove_task_from_sprint(self):
		task_id = list(self.tp.all_tasks['feature'].keys())[0]
		id = list(self.tp.all_sprints.keys())[0]
		self.tp.add_task_to_sprint(id, task_id)
		self.tp.remove_task_from_sprint(id, task_id)
		count = 0
		for key, value in self.tp.all_sprints.items():
			for task in value:
				count += 1
		self.assertEqual(count, 0)
			
			
def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestTaskPlanner('test_create_task'))
	suite.addTest(TestTaskPlanner('test_create_subtrack'))
	suite.addTest(TestTaskPlanner('test_get_task'))
	suite.addTest(TestTaskPlanner('test_create_sprint'))
	suite.addTest(TestTaskPlanner('test_remove_sprint'))
	suite.addTest(TestTaskPlanner('test_add_task_to_sprint'))
	suite.addTest(TestTaskPlanner('test_remove_task_from_sprint'))
	return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
'''if __name__ == "__main__":
		unittest.main()
'''

