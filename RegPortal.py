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

def do_login(user, prompt_func):
	logged_in = user.is_logged_in()
	if not logged_in:
		pw = prompt_func(prompt='Please enter your password: ')
		logged_in = user.login(pw)

	if logged_in:
		print('\nWelcome!\n')
	else:
		print('Invalid credentials.  Please try again.')
		do_login(user, prompt_func)

def user_do(user, cmd):
	method = user.do(cmd)
	output = method()
	if output:
		print(output)

def portal_view(user=None):
	if not user:
		print('OPTIONS:\n', '\tlogin\n', '\tquit\n')
		cmd = input('Enter a command: ')
		if cmd == 'login':
			while not user:
				email = input('Please enter your email: ')
				user = get_user_object(email)
			do_login(user, getpass.getpass)
			portal_view(user)
		elif cmd == 'quit':
			print('Goodbye!')
		else:
			print('Invalid command.  Please try again.')
			portal_view()
	else:
		user.show_info()
		while user.is_logged_in():
			cmd = input('Enter a command: ')
			user_do(user, cmd)
			print('------')
		else:
			portal_view()


if __name__ == '__main__':
	portal_view()


