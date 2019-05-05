# Employee Management System
# Author		:	John Lee
# Creation Date :	5/5/2019
# Last Updated	:	5/5/2019

# Employee
# __name, __department, __job_title
# get_name(), get_department(), get_job_title()
# set_name(name), set_department(department), set_job_title(job_title)

# import libraries
import IOExceptions
import pickle

# Initialize menu constants
LOOK_UP = 1
ADD_EMPLOYEE = 2
CHANGE_EMPLOYEE = 3
DELETE_EMPLOYEE = 4
QUIT = 5

# Initialize constants
FILE_NAME = 'employee.dat'

# Create employee class
class Employee():

	def __init__(self, name, department, job_title):
		self.__name = name
		self.__department = department
		self.__job_title = job_title

	def get_name(self):
		return self.__name

	def get_department(self):
		return self.__department

	def get_job_title(self):
		return self.__job_title

	def set_name(self, name):
		self.__name = name

	def set_department(self, department):
		self.__department = department

	def set_job_title(self, job_title):
		self.__job_title = job_title

	def __str__(self):
		return "\nName : " + self.__name + "\nDepartment : " + self.__department + "\nJob Title : " + self.__job_title

def main():

	# Initialize dict to store employees
	employees = {}

	# Initialize menu choice
	menu_choice = 0

	# Load pickled objects from file into dict
	employees = load_file(FILE_NAME)

	# Display menu and get user choice
	menu_choice = get_menu_choice()

	while menu_choice != QUIT:
		# Look up employee
		if menu_choice == 1:
			look_up_employee(employees)

		# Add employee
		elif menu_choice == 2:
			add_employee(employees)

		# Change Employee info
		elif menu_choice == 3:
			change_employee_info(employees)

		# Delete employee
		elif menu_choice == 4:
			delete_employee(employees)

		menu_choice = get_menu_choice()

	# Quit program
	save_and_quit(employees)

def load_file(file_name):

	# initialize var
	file_mode = 'rb'
	
	# try opening file
	file_open_result = IOExceptions.open_file(file_name, file_mode)

	if file_open_result == 0:
		with open(file_name, file_mode) as opened_file:
			try:
				return pickle.load(opened_file)
			except:
				return {}

	else:
		return {}

def get_menu_choice():

	# Display menu
	print("\nMenu\n1 = Look up Employee \n2 = Add Employee \n3 = Change Employee Info \n4 = Delete Employee \n5 = Quit\n")

	# Get user choice
	choice = input('Choose a menu option : ')

	# Input validation
	while choice.isdigit() == False or int(choice) < LOOK_UP or int(choice) > QUIT:
		choice = input('Enter valid menu option : ')

	return int(choice)

def look_up_employee(employees):

	# Get employee name
	name = input('Enter employee name : ')

	# Look up employee
	employee_info = employees.get(name, 'Name not found.')

	print(employee_info)

def add_employee(employees):

	# get name
	name = input("Enter employee's name : ")

	# get department
	department = input("Enter employee's department : ")

	# get job title
	job_title = input("Enter employee's job title : ")

	# create employee object instance
	employee = Employee(name, department, job_title)

	# add to employees dict
	if name not in employees:
		employees[name] = employee
		print('%s has been added as an employee.' % name)
	else:
		print("%s already exists as an employee." % name)

def change_employee_info(employees):

	# Get employee name
	name = input("Enter employee's name : ")

	# If employee name exists ask for department and job title
	if name in employees:
		department = input("Enter employee's department : ")
		job_title = input("Enter employee's job title : ")
		
		# Change info
		employee = Employee(name, department, job_title)
		employees[name] = employee

	# If employee does not exist, then pass
	else:
		print("%s does not exist." % name)

def delete_employee(employees):

	# Get employee name
	name = input("Enter employee's name : ")

	# If employee name exists ask for department and job title
	if name in employees:
		del employees[name]
		print("%s successfully deleted." % name)

	# If employee does not exist, then pass
	else:
		print("%s does not exist." % name)

def save_and_quit(employees):
	file_mode = 'wb'

	# try opening file
	file_open_result = IOExceptions.open_file(FILE_NAME, file_mode)

	if file_open_result == 0:
		# Open file for writing
		with open(FILE_NAME, file_mode) as opened_file:
			# Pickle dictionary and save it
			pickle.dump(employees, opened_file)

# Run program
main()

# END OF PROGRAM