import unittest

import RegPortal
from Users import User, Student, Professor, RegistrationManager


class TestRegPortal(unittest.TestCase):

	def setUp(self):
		self.email_func = lambda x: 'test@student.com'
		self.pass_func = lambda: 'teststudent'
		self.show_name_cmd = lambda: 'show_name'
		self.logout_cmd = lambda: 'logout'

		self.test_student = Student(
			'test_major', 2006,
			'Test', 'Student',
			email='test@student.com', password='teststudent')

		self.test_prof = Professor(
			'test_college', 'Howie L4',
			'Dr.', 'Test',
			email='test@prof.com', password='testprof'
			)

		self.test_regm = RegistrationManager(
			'test_first_name', 'Test',
			email='test@regm.com', password='testregm'
			)

	def test_get_user_object(self):
		self.assertEqual(RegPortal.get_user_object('test@student.com').major, self.test_student.major)
		self.assertEqual(RegPortal.get_user_object('test@prof.com').college, self.test_prof.college)
		self.assertEqual(RegPortal.get_user_object('test@regm.com').first_name, self.test_regm.first_name)
		self.assertEqual(RegPortal.get_user_object('bogus'), None)

	def test_manage_login(self):
		self.assertEqual(
			RegPortal.manage_login(email_func=self.email_func, pass_func=self.pass_func).major,
			self.test_student.major)

	def test_do_login(self):
		self.assertFalse(self.test_student.is_logged_in(), msg='test_student was already logged in')
		self.assertTrue(RegPortal.do_login(self.test_student, pass_func=self.pass_func))
		self.assertFalse(RegPortal.do_login(self.test_prof, pass_func=self.pass_func))

	def test_manage_session(self):
		pass

	def test_portal_view(self):
		pass


class TestUserMethods(unittest.TestCase):

	def setUp(self):
		self.user = User('Foo', 'Bar', email='mymail@me.com', password='password')
		self.user_no_pw = User('Foo', 'Bar', email='mymail@me.com')

	def test_initialization(self):
		self.assertEqual(self.user.first_name, 'Foo')
		self.assertEqual(self.user.last_name, 'Bar')
		self.assertEqual(self.user.email, 'mymail@me.com')
		self.assertEqual(self.user.password, 'password')
		self.assertNotEqual(self.user_no_pw.password, None)
		self.assertEqual(self.user.logged_in, False)

	def test_set_name(self):
		self.user.set_name(lambda x: 'New', lambda x: 'Name')
		self.assertEqual(self.user.first_name, 'New')
		self.assertEqual(self.user.last_name, 'Name')

	def test_get_name(self):
		name = self.user.get_name()
		self.assertEqual(name, 'Foo Bar')

	def test_set_email(self):
		self.user.set_email(lambda x: 'mynewemail@domain.com')
		self.assertEqual(self.user.email, 'mynewemail@domain.com')

	def test_set_password(self):
		self.user.set_password('NewPassword')
		self.assertEqual(self.user.password, 'NewPassword')

		pw = self.user.set_password()
		self.assertEqual(self.user.password, pw)

	def test_login(self):
		pass

	def test_logout(self):
		pass

	def test_is_logged_in(self):
		pass




if __name__ == '__main__':
	unittest.main()
