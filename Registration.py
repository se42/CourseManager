import datetime

class RegistrationForm:
	"""docstring for RegistrationForm"""

	instances = []

	def __init__(self, student):
		self.student = student
		self.date_created = datetime.date.today()
		self.last_updated = None
		self.semester = None
		self.preferences = []
		RegistrationForm.instances.append(self)

	def set_preference(self, section):
		self.preferences.append(section)

		