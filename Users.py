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

	def show_info(self):
		print('set_name\tChange your name')
		print('show_name\tShow your name')
		print('set_email\tChange your email')
		print('show_email\tShow your email')
		print('show_info\tShow this info again')
		print('logout\t\tLog out of the system')

	def get_cmds(self):
		"""
		Child classes should call this and add their own
		methods to this dictionary, then return the newly
		created dictionary.
		"""
		commands = {
			'set_name': self.set_name,
			'show_name': self.get_name,
			'set_email': self.set_email,
			'show_email': self.get_email,
			'show_info': self.show_info,
			'logout': self.logout,
		}
		return commands

	def do(self, cmd):
		"""
		First assemble a child-class-specific dictionary of commands,
		then attempt to access that dictionary to retrieve the
		requested method.  Return a callable lambda function with
		and error message if command does not exist as typed.
		"""
		commands = self.get_cmds()
		try:
			method = commands[cmd]
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
		print('Logged in as: ', self.get_name())
		print('Current email: ', self.get_email())
		print('Your major: ', self.major)
		print('Your sections: ', self.sections_taken)
		print('------')
		print('User Actions:')
		super(Student, self).show_info()
		print()
		print('Student Actions')
		print('show_major\tShow your major')
		print('set_major\tChange your major')
		print()

	def get_cmds(self):
		commands = super(Student, self).get_cmds()
		commands['show_major'] = self.get_major
		commands['set_major'] = self.set_major
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
		print('Logged in as: ', self.get_name())
		print('Current email: ', self.get_email())
		print('Your college: ', self.college)
		print('Your office: ', self.office_number)
		print('Your courses:')
		for each in self.courses_taught:
			print('\t', end='')
			print(each)
		print('------')
		print('User Actions:')
		super(Professor, self).show_info()
		print()
		print('Professor Actions')
		print('set_college\tChange your college')
		print('set_office\tChange your office number')
		print('create_course\tCreate a new course')
		print('show_rosters\tShow your rosters')
		print()

	def get_cmds(self):
		commands = super(Professor, self).get_cmds()
		commands['set_college'] = self.set_college
		commands['set_office'] = self.set_office
		commands['create_course'] = self.create_course
		return commands


class RegistrationManager(User):
	"""docstring for RegistrationManager"""
	def __init__(self, *args, **kwargs):
		super(RegistrationManager, self).__init__(*args, **kwargs)

	def enroll_student(self, Student, Course):
		pass

	def suspend_student(self, Student):
		pass

	def run_scheduler(self):
		pass
