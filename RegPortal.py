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

	if not logged_in:
		do_login(user, prompt_func)

def user_do(user, cmd):
	method = user.do(cmd)
	output = method()
	if output:
		print(output)


if __name__ == '__main__':
	user = None
	while not user:
		email = input('Please enter your email: ')
		user = get_user_object(email)
	do_login(user, getpass.getpass)
	print('\nWelcome!\n')
	user.show_info()
	while user.is_logged_in():
		cmd = input('Enter a command: ')
		user_do(user, cmd)
		print('------')
	print('Goodbye!')


