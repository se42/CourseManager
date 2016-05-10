import unittest

from Users import User, Student, Professor, RegistrationManager

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
