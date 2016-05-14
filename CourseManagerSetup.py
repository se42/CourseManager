"""
Import this file into a Python shell session to set up a small
set of User and Course objects.  Use import * so object variables
are imported:

	from CourseManagerSetup.py import *

"""
import datetime

from Users import Student, Professor, RegistrationManager
from Courses import Course, Section
from Registration import RegistrationForm


## Define some Users
scott = Student(
	'Biochemistry', 2006,
	'Scott', 'Edwards',
	email='scott@scott.com', password='scottword'
	)
suzie = Student(
	'Computer Science', 2008,
	'Suzie', 'Jacobs',
	email='suzie@suzie.com', password='suzieword'
	)
jake = Student(
	'Computer Science', 2008,
	'Jake', 'Smith',
	email='jake@jake.com', password='jakeword'
	)
mary = Student(
	'Chemistry', 2007,
	'Mary', 'Ford',
	email='mary@mary.com', password='maryword'
	)
tom = Student(
	'Magic', 2002,
	'Tom', 'Riddle',
	email='tom@tom.com', password='horcrux'
	)
harry = Student(
	'Potions', 2008,
	'Harry', 'Potter',
	email='harry@harry.com', password='fatlady'
	)
led = Student(
	'Rock', 1975,
	'Led', 'Zeppelin',
	email='led@led.com', password='gettheledout'
	)
john = Student(
	'Math', 1923,
	'John', 'von Neumann',
	email='john@john.com', password='smartypants'
	)

albert = Professor(
	'Physics', 'Howie 3108',
	'Albert', 'Einstein',
	email='albert@albert.com', password='relativity'
	)
emmett = Professor(
	'Time Travel', 'DeLorean 121',
	'Emmett', 'Brown',
	email='doc@doc.com', password='gigawatts'
	)

regis = RegistrationManager(
	'Regis', 'Manfred',
	email='regis@regis.com', password='magicword'
	)

## Test users -- DON'T CHANGE THESE!
test_student = Student(
	'test_major', 2006,
	'Test', 'Student',
	email='test@student.com', password='teststudent'
	)
test_prof = Professor(
	'test_college', 'Howie L4',
	'Dr.', 'Test',
	email='test@prof.com', password='testprof'
	)
test_regm = RegistrationManager(
	'test_first_name', 'Test',
	email='test@regm.com', password='testregm'
	)


## Define some Courses and Sections
cs101 = Course('Intro to CS', 'CS101', 3, emmett)
emmett.courses_taught.append(cs101)
phys302 = Course('Advanced Physics', 'PHYS302', 3, albert)
albert.courses_taught.append(phys302)

cs101_a = Section(cs101, 'A')
cs101_a.set_location('Klaus 101')
cs101_a.set_time('MWF 9:05')
cs101_b = Section(cs101, 'B')
cs101_b.set_location('Klaus 215')
cs101_b.set_time('TR 8:05')
phys302_a = Section(phys302, 'A')
phys302_a.set_location('Howie L4')
phys302_a.set_time('MWF 10:05')
phys302_b = Section(phys302, 'B')
phys302_b.set_location('Howie L4')
phys302_b.set_time('TR 8:05')


## Object lists
students = [scott, suzie, jake, mary, tom, harry, led, john, test_student]
professors = [albert, emmett, test_prof]
courses = [cs101, phys302]
sections = [cs101_a, cs101_b, phys302_a, phys302_b]


## Give every student a RegistrationForm
for each in students:
	RegistrationForm(each)


## Dictionary to be used instead of a database
db = {
	'students': students,
	'professors': professors,
	'regman': [regis, test_regm],
	'courses': courses,
	'sections': sections,
}
