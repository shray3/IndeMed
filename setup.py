import manage, db
import test
import os

if __name__ == '__main__':
	os.system('python manage.py flush')
	os.system('python manage.py makemigrations')
	os.system('python manage.py migrate')
	os.system('python manage.py syncdb')
	db.populate()