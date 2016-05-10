

class Course:
	"""docstring for Course"""
	def __init__(self, name, course_number, credits, professor):
		self.name = name
		self.course_number = course_number
		self.credits = credits
		self.professor = professor
		self.sections = []

	def __str__(self):
		return self.course_number + ' -- ' + self.name

	def open(self):
		"""Return True if course has an open section, False if not."""
		for each in self.sections:
			if each.open() == True:
				return True
			else:
				pass
		return False

	def add_section(self, section):
		self.sections.append(section)


class Section:
	"""docstring for Section"""
	def __init__(self, course, section_number):
		self.course = course
		self.section_number = section_number
		self.location = 'TBD'
		self.time = 'TBD'
		self.roster = []
		self.roster_max = 4

		self.course.add_section(self)

	def open(self):
		"""Return True if section is open, False if not."""
		if len(self.roster) <= self.roster_max:
			return True
		else:
			return False

	def add_student(self, student):
		self.roster.append(student)

	def get_roster(self):
		return self.roster

	def set_location(self, location):
		self.location = location

	def set_time(self, time):
		self.time = time
