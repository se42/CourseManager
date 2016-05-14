"""
Definiton of various User classes.
"""

import random
import string

from Courses import Course, Section
from Registration import RegistrationForm


class User:
	"""docstring for User"""
	def __init__(self, first_name, last_name, email=None, password=None):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.logged_in = False

		if not password:
			self.set_password()

		if not email:
			email = input('Please provide an email address: ')
			self.set_email(email)

	def __str__(self):
		return self.get_name()

	def set_name(self, input_func1=input, input_func2=input):
		self.first_name = input_func1('Enter first name: ')
		self.last_name = input_func2('Enter last name: ')
		return None

	def get_name(self):
		return self.first_name + ' ' + self.last_name

	def set_email(self, input_func=input):
		self.email = input_func('Enter new email: ')
		return 'Email set to: {0}'.format(self.email)

	def get_email(self):
		return self.email

	def set_password(self, password=None):
		if password:
			self.password = password
		else:
			chars = string.ascii_letters
			password = []
			for each in range(4):
				i = random.randint(0, len(chars) -1)
				password.append(chars[i])
			self.password = ''.join(password)
		return self.password

	def login(self, password):
		if password == self.password:
			self.logged_in = True
			return True
		else:
			return False

	def logout(self, *args, **kwargs):
		self.logged_in = False
		if not self.logged_in:
			return 'Logout successful.'
		else:
			return 'Logout failed.'

	def is_logged_in(self):
		return self.logged_in

	def get_base_info(self):
		info = [
			'Logged in as: {0}'.format(self.get_name()),
			'Current email: {0}'.format(self.get_email()),
		]
		return info

	def get_base_cmds(self):
		# these are the commands that will be shown when show_info is called
		base_cmds = [
			'set_name',
			'show_name',
			'set_email',
			'show_email',
			'show_info',
			'logout',
			]
		return base_cmds

	def get_cmds(self):
		"""
		These are the commands that are "installed" and available to be called.
		
		Child classes should call this and add their own
		methods to the returned dictionary, then return a
		newly created dictionary.
		"""
		commands = {
			'set_name': {
				'command': self.set_name,
				'message': 'set_name\tChange your name',
				},
			'show_name': {
				'command': self.get_name,
				'message': 'show_name\tShow your name',
				},
			'set_email': {
				'command': self.set_email,
				'message': 'set_email\tChange your email',
				},
			'show_email': {
				'command': self.get_email,
				'message': 'show_email\tShow your email',
				},
			'show_info': {
				'command': self.show_info,
				'message': 'show_info\tShow this info again',
				},
			'logout': {
				'command': self.logout,
				'message': 'logout\t\tLog out of the system',
				},
		}
		return commands

	def show_info(self):
		# print all base info
		for each in self.get_base_info():
			print(each)
		# print base user actions
		print('User Actions:')
		commands = self.get_cmds()
		for each in self.get_base_cmds():
			print(commands[each]['message'])
		print()

	def do(self, cmd):
		"""
		First assemble a child-class-specific dictionary of commands,
		then attempt to access that dictionary to retrieve the
		requested method.  Return a callable lambda function with
		and error message if command does not exist as typed.
		"""
		commands = self.get_cmds()
		try:
			method = commands[cmd]['command']
		except KeyError:
			method = lambda: 'Command does not exist as typed.'
		return method


class Student(User):
	"""docstring for Student"""
	def __init__(self, major, matriculated, *args, **kwargs):
		self.major = major
		self.matriculated = matriculated
		self.suspended = False
		self.registration_form = RegistrationForm(self)
		self.sections_taken = []
		super(Student, self).__init__(*args, **kwargs)

	def get_major(self):
		return self.major

	def set_major(self, input_func=input):
		self.major = input_func('Enter new major: ')
		return 'Major changed to {0}'.format(self.major)

	def register(self, preference_list):
		"""
		Update registration form prior to Scheduler run time.
		preference_list is a list of Section objects ranked
		from most preferred to least preferred
		"""
		for each in preference_list:
			self.registration_form.set_preference(each)

	def add_course(self, course):
		"""Add course directly during open registration"""
		if course.open():
			# present open sections for selection
			pass
		else:
			print('Course is closed.')

	def drop_course(self, section):
		# remove course from Student sections list
		# needs partner to remove student from Section roster
		pass

	def get_sections(self):
		pass

	def show_info(self):
		# print all base info
		for each in self.get_base_info():
			print(each)
		# print student-specific info
		print('Your major: ', self.major)
		print('Your sections: ', self.sections_taken)
		print('------')
		# print base user actions
		print('User Actions:')
		commands = self.get_cmds()
		for each in self.get_base_cmds():
			print(commands[each]['message'])
		print()
		# print student-specific actions
		print('Student Actions')
		for each in self.get_student_cmds():
			print(commands[each]['message'])
		print()

	def get_student_cmds(self):
		# active student commands
		student_cmds = [
			'show_major',
			'set_major',
		]
		return student_cmds

	def get_cmds(self):
		commands = super(Student, self).get_cmds()
		commands['show_major'] = {
			'command': self.get_major,
			'message': 'show_major\tShow your major',
			}
		commands['set_major'] = {
			'command': self.set_major,
			'message': 'set_major\tChange your major',
			}
		return commands



class Professor(User):
	"""docstring for Professor"""
	def __init__(self, college, office_number, *args, **kwargs):
		self.college = college
		self.office_number = office_number
		self.courses_taught = []
		super(Professor, self).__init__(*args, **kwargs)

	def set_college(self, input_func=input):
		self.college = input_func('Enter new college: ')

	def set_office(self, input_func=input):
		self.office_number = input_func('Enter new office: ')

	def get_rosters(self):
		print('Rosters shown')

	def create_course(self, input_func1=input, input_func2=input, input_func3=input):
		name = input_func1('Enter course name: ')
		number = input_func2('Enter course number: ')
		credits = input_func3('Enter number of credits: ')
		course = Course(name, number, credits, self)
		self.courses_taught.append(course)

	def show_info(self):
		# print all base info
		for each in self.get_base_info():
			print(each)
		# print professor-specific info
		print('Your college: ', self.college)
		print('Your office: ', self.office_number)
		print('Your courses:')
		for each in self.courses_taught:
			print('\t', end='')
			print(each)
		print('------')
		# print base user actions
		print('User Actions:')
		commands = self.get_cmds()
		for each in self.get_base_cmds():
			print(commands[each]['message'])
		print()
		# print professor-specific actions
		print('Professor Actions')
		for each in self.get_professor_cmds():
			print(commands[each]['message'])
		print()

	def get_professor_cmds(self):
		# active professor commands
		professor_cmds = [
			'set_college',
			'set_office',
			'create_course',
			'show_rosters',
		]
		return professor_cmds

	def get_cmds(self):
		commands = super(Professor, self).get_cmds()
		commands['set_college'] = {
			'command': self.set_college,
			'message': 'set_college\tChange your college',
			}
		commands['set_office'] = {
			'command': self.set_office,
			'message': 'set_office\tChange your office number',
			}
		commands['create_course'] = {
			'command': self.create_course,
			'message': 'create_course\tCreate a new course',
			}
		commands['show_rosters'] = {
			'command': self.get_rosters,
			'message': 'show_rosters\tShow your rosters',
		}
		return commands


class RegistrationManager(User):
	"""docstring for RegistrationManager"""
	def __init__(self, *args, **kwargs):
		super(RegistrationManager, self).__init__(*args, **kwargs)

	def enroll_student(self):
		print('Enroll student...')

	def suspend_student(self):
		print('Suspend student...')

	def run_scheduler(self):
		print('Run scheduler...')

	def show_info(self):
		# print all base info
		for each in self.get_base_info():
			print(each)
		print('------')
		# print base user actions
		print('User Actions:')
		commands = self.get_cmds()
		for each in self.get_base_cmds():
			print(commands[each]['message'])
		print()
		# print professor-specific actions
		print('Registration Manager Actions')
		for each in self.get_regman_cmds():
			print(commands[each]['message'])
		print()

	def get_regman_cmds(self):
		# active professor commands
		regman_cmds = [
			'enroll_student',
			'suspend_student',
			'run_scheduler',
		]
		return regman_cmds

	def get_cmds(self):
		commands = super(RegistrationManager, self).get_cmds()
		commands['enroll_student'] = {
			'command': self.enroll_student,
			'message': 'enroll_student\tEnroll a new student',
			}
		commands['suspend_student'] = {
			'command': self.suspend_student,
			'message': 'suspend_student\tSuspend a student from registration activities',
			}
		commands['run_scheduler'] = {
			'command': self.run_scheduler,
			'message': 'run_scheduler\tRun the automated scheduling tool',
			}
		return commands
