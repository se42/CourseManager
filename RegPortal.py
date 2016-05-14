import datetime
import getpass

# CourseManagerSetup import provides lists of objects instead
# of going through the trouble of managing a database
from CourseManagerSetup import db


def get_user_object(email):
	for user in (db['students'] + db['professors'] + db['regman']):
		if user.email == email:
			return user
	print('Could not find user.  Please try again.')

def manage_login(email_func=input, *args, **kwargs):
	user = None
	while not user:
		email = email_func('Please enter your email: ')
		user = get_user_object(email)
	do_login(user, *args, **kwargs)
	if user.is_logged_in():
		return user
	else:
		return None

def do_login(user, pass_func=getpass.getpass, tries=3):
	logged_in = user.is_logged_in()
	if not logged_in:
		pw = pass_func()
		logged_in = user.login(pw)

	if logged_in:
		print('\nWelcome!\n')
		return True
	else:
		tries -= 1
		print('Invalid credentials.  {0} tries remaining.'.format(tries))
		if tries > 0:
			do_login(user, pass_func=pass_func, tries=tries)
		else:
			return False

def manage_session(user, input_func=input):
	user.show_info()
	while user.is_logged_in():
		cmd = input_func('Enter a command: ')
		method = user.do(cmd)
		output = method()
		if output:
			print(output)
		print('------')

def portal_view():
	print('Welcome to the Course Manager Application!\n')
	print('OPTIONS:\n', '\tlogin\n', '\tquit\n')
	cmd = input('Enter a command: ')
	if cmd == 'login':
		user = manage_login()
		if user:
			manage_session(user)
		portal_view()
	elif cmd == 'quit':
		print('Goodbye!')
	else:
		print('Invalid command.  Please try again.')
		portal_view()


if __name__ == '__main__':
	portal_view()


