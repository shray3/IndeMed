import os
import django
import datetime
import hashlib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "indmed.settings")

from polls.models import *

#Code to populate the database for testing the IndeMed Project

def populate():
	print '--- starting practice ---'

	practice1 = Practice.objects.create(name = "Practice1")
	practice2 = Practice.objects.create(name = "Practice2")

	print '--- added 2 practices ---'

	print '--- starting institutions ---'

	masonic = Institution.objects.create(name = 'Masonic Home', address = '1001 Masonic Drive, Philadelphia PA 19104', interface = 'email1', practice = practice1)
	dv = Institution.objects.create(name = 'Deer Valley', address = '1001  Valley Road, Philadelphia PA 19104', interface = 'email2', practice = practice1)
	AHomes = Institution.objects.create(name = 'American Homes', address = '1003 Amway Homes, Philadelphia PA 19104', interface = 'email3', practice = practice1)
	ExcelHomes = Institution.objects.create(name = 'Excellence Homes', address = '1003 Excellence Road, Philadelphia PA 19104', interface = 'email4', practice = practice1)

	print ('--- adding doctors --- ')

	sandeep = add_doctor(first = 'Sandeep', last ='Kapoor', addr = '2109 Club Vista Place, Philadelphia, PA 19104', practice = practice1, email = 'sandeep@gmail.com')
	sangeeta  = add_doctor(first = 'Sangeeta', last = 'Kapoor', addr = '2109 Club Vista Drive, Philadelphia, PA 19104', practice = practice1, email = 'sangeeta@gmail.com')
	sanjay = add_doctor(first = 'Sanjay', last = 'Jain', addr = '10920 Fairway Pointe Drive, Philadelphia, PA 19104', practice = practice1, email = 'sanjay@gmail.com')
	muhummad = add_doctor(first = 'Muhummad', last = 'Babar', addr = '1900 Brotherly Love Drive, Philadelphia, PA', practice = practice1, email = 'muhummad@gmail.com')
	richa = add_doctor(first = 'Richa', last = 'Gupta', addr = '1900 Walnut Drive, Philadelphia, PA', practice = practice1, email = 'richa@gmail.com')

	print ('---- added 5 doctors ----')

	print ('---- adding nurses ---')

	kathy = add_nurse(first = 'Katherine', last = 'Atwood', addr = '100 Oak Hill Road, Philadelphia, PA 19104', practice = practice1, email = 'kathy@gmail.com')
	margaret = add_nurse (first = 'Margaret', last = 'Thatcher', addr = '10923 Fairway Drive, Philadelphia, PA 19104', practice = practice1, email = 'margaret@gmail.com')
	laura = add_nurse (first = 'Laura', last = 'Thomas', addr = '3923 Spruce Street, Philadelphia, PA 19104', practice = practice1, email = 'laura@gmail.com')
	sydney = add_nurse (first = 'Sydney', last = 'Johnson', addr = '3920 Walnut Street, Philadelphia, PA 19104', practice = practice1, email = 'sydney@gmail.com')
	danica = add_nurse (first = 'Danica', last = 'Allison', addr = '4001 Walnut Street, Philadelphia, PA 19104', practice = practice1, email = 'danica@gmail.com')
	allison = add_nurse (first = 'Allison', last = 'Daniels', addr = '3900 Walnut Street, Philadelphia, PA 19104', practice = practice1, email = 'allison@gmail.com')
	jessica = add_nurse (first = 'jessica', last = 'Downey', addr = '17 Market Street, Philadelphia, PA 19104', practice = practice1, email = 'jessica@gmail.com')

	print ('---- added 7 nurses ----')

	print '--- creating login ---'

	login1 = LogIn.objects.create(person = sandeep.person, email = 'sandeep@gmail.com', password = hashPassword('sandeep'), practice = practice1)
	login2 = LogIn.objects.create(person = sangeeta.person, email = 'sangeeta@gmail.com', password = hashPassword('sangeeta'), practice = practice1)
	login3 = LogIn.objects.create(person = sanjay.person, email = 'sanjay@gmail.com', password = hashPassword('sanjay'), practice = practice1)
	login4 = LogIn.objects.create(person = muhummad.person, email = 'muhummad@gmail.com', password = hashPassword('muhummad'), practice = practice1)
	login5 = LogIn.objects.create(person = richa.person, email = 'richa@gmail.com', password = hashPassword('richa'), practice = practice1)

	nlogin1 = LogIn.objects.create(person = kathy.person, email = 'kathy@gmail.com', password = hashPassword('kathy'), practice = practice1)
	nlogin2 = LogIn.objects.create(person = margaret.person, email = 'margaret@gmail.com', password = hashPassword('margaret'), practice = practice1)
	nlogin3 = LogIn.objects.create(person = laura.person, email = 'laura@gmail.com', password = hashPassword('laura'), practice = practice1)
	nlogin4 = LogIn.objects.create(person = sydney.person, email = 'sydney@gmail.com', password = hashPassword('sydney'), practice = practice1)
	nlogin5 = LogIn.objects.create(person = danica.person, email = 'danica@gmail.com', password = hashPassword('danica'), practice = practice1)
	nlogin6 = LogIn.objects.create(person = allison.person, email = 'allison@gmail.com', password = hashPassword('allison'), practice = practice1)
	nlogin7 = LogIn.objects.create(person = jessica.person, email = 'jessica@gmail.com', password = hashPassword('jessica'), practice = practice1)

	print '--- added 5 logins for all the doctors ---'

	person = models.OneToOneField(Person)
	email = models.EmailField(max_length = 50)
	password = models.CharField(max_length = 50)
	practice = models.ForeignKey(Practice)
	

	print ('--- adding 15 billing informations ----')

	b1 = add_billing(billing_no = '428859', plan = 'Family', company = 'Aetna')
	b2 = add_billing(billing_no = '331727', plan = 'Individual', company = 'Blue Cross')
	b3 = add_billing(billing_no = '135557', plan = 'Individual Plus', company = 'Blue Shield')
	b4 = add_billing(billing_no = '904880', plan = 'Individual Plus', company = 'Humana')
	b5 = add_billing(billing_no = '477475', plan = 'Basic', company = 'Blue Cross')
	b6 = add_billing(billing_no = '374987', plan = 'Advanced', company = 'Humana')
	b7 = add_billing(billing_no = '638633', plan = 'Family', company = 'Aetna')
	b8 = add_billing(billing_no = '633781', plan = 'Basic', company = 'Blue Shield')
	b9 = add_billing(billing_no = '643744', plan = 'Individual', company = 'UnitedHealth')
	b10 = add_billing(billing_no = '387259', plan = 'Family', company = 'Humana')
	b11 = add_billing(billing_no = '198625', plan = 'Basic', company = 'Anthem')
	b12 = add_billing(billing_no = '819511', plan = 'Family', company= 'Humana')
	b13 = add_billing(billing_no = '288950', plan = 'Individual Plus', company = 'Aetna')
	b14 = add_billing(billing_no = '853621', plan = 'Family', company = 'Blue Shield')
	b15 = add_billing(billing_no = '341689', plan = 'Family', company = 'Anthem')

	print ('--- added 15 billing statuses for each of the patients ---')

	print ('--- adding patients ---')

	p1 = add_patient (first = 'Lisa', last = 'Phillips', address = '7475 Quiet Rabbit Wynd, Unicorn, PA 18955', dob = datetime.datetime(1965, 2,25), phone = '555(5555)', description = 'Common cold with complications', institution = masonic, doctor = sandeep, nurse = allison, practice = practice1, billing = b1)
	p2 = add_patient (first = 'Tina', last = 'Parker', address = '5441 Pleasant Pond Loop, Beauty Spot, PA 17473',dob = datetime.datetime(1946, 3, 11), phone = '555(5432)', description = 'Recovering from hip replacement surgery', institution = masonic, doctor = sandeep, nurse = danica, practice = practice1, billing = b2)
	p3 = add_patient (first = 'Theresa', last = 'Hughes', address = '6272 Rockytownline, Blowing Cave, PA 19609', dob = datetime.datetime(1945, 7,27), phone = '155(9832)', description = 'Influenza', institution = masonic, doctor = sandeep, nurse = danica, practice = practice1, billing = b3)
	p4 = add_patient (first = 'Angela', last = 'Wright', address = '4860 Foggy Creek Bend,  Rendezvous,  PA  15560-7092', dob = datetime.datetime(1955, 5, 25), phone = '555(1234)', description = 'Headaches and nausea', institution = masonic, doctor = muhummad, nurse = allison, practice = practice1, billing = b4)
	p5 = add_patient (first = 'Lori', last = 'Franklin', address = '8768 Clear Pines,  Carlyle,  PA  16462-3194', dob = datetime.datetime(1959, 9, 19), phone = '554(5321)', description = 'Glaucoma', institution = dv, doctor = sanjay, nurse = danica, practice = practice1, billing = b5)
	p6 = add_patient (first = 'Joe', last = 'Diaz', address = '3906 Burning Mountain,  Big Hammock,  PA  18985-4893', dob = datetime.datetime(1965, 10,10), phone = '444(8521)', description = 'Alcoholism', institution = dv, doctor = sanjay, nurse = danica, practice = practice1, billing = b6)
	p7 = add_patient (first = 'Virginia', last = 'Roberts', address = '4490 Wishing Bear Stead,  Delightful,  PA  15033-7451', dob = datetime.datetime(1954, 6,6), phone = '777(7777)', description = 'Drug dependencies' , institution = ExcelHomes, doctor = sanjay, nurse = sydney, practice = practice1, billing = b7)
	p8 = add_patient (first = 'Matthew', last = 'Cruz', address = '3040 Blue Valley,  Spunky Puddle,  PA  17623-2711', dob = datetime.datetime(1971, 9, 18), phone = '888(8888)', description = 'Social Media addiction', institution = dv, doctor = sanjay, nurse = sydney, practice = practice1, billing = b8)
	p9 = add_patient (first = 'Ryan', last = 'Palmer', address = '9137 Shady Acres,  Mount Cuba,  PA  19304-4051', dob = datetime.datetime(1955, 8, 17), phone = '999(9999)', description = 'Hypertension', institution = dv, doctor = sanjay, nurse = sydney, practice = practice1, billing = b9)
	p10 = add_patient (first = 'Debra', last = 'Hill', address = '7582 Noble Point,  Nummytown,  PA  18790-7007', dob = datetime.datetime(1950, 3, 23), phone = '456(1234)', description = 'Meningitis', institution = AHomes, doctor = richa, nurse = jessica, practice = practice1, billing = b10)
	p11 = add_patient (first = 'Kathryn', last = 'Brown', address = '8897 Tawny Route,  Eston,  PA  19131-5682', dob = datetime.datetime(1965, 5, 14), phone = '666(5464)', description = 'HIV', institution = AHomes, doctor = richa, nurse = jessica, practice = practice1, billing = b11)
	p12 = add_patient (first = 'Albert', last = 'Evans', address = '6394 Hidden Cider Highlands,  Savona,  PA  18200-0024', dob = datetime.datetime(1950, 5,5), phone = '795(1234)', description = 'Diabetes', institution = AHomes, doctor = richa, nurse = jessica, practice = practice1, billing = b12)
	p13 = add_patient (first = 'Kevin', last = 'Williamson', address = '3043 Honey Prairie Manor,  Loves Corner,  PA  19339-9301', dob = datetime.datetime(1945, 6, 16), phone = '987(5463)', description = 'Kidney Disease', institution = ExcelHomes, doctor = sangeeta, nurse = sydney, practice = practice1, billing = b13)
	p14 = add_patient (first = 'Lawrence', last = 'Morrison', address = '8144 Stony Vista,  Dinosaur,  PA  15707-0840', dob = datetime.datetime(1950, 7, 27), phone = '879(1234)', description = 'HPV', institution = ExcelHomes, doctor = sangeeta, nurse = sydney, practice = practice1, billing = b14)
	p15 = add_patient (first = 'Theresa', last = 'Sanchez', address = '422 Iron Circuit,  Cutlips,  PA  15926-9287', dob = datetime.datetime(1965, 2, 12), phone = '844(1597)', description = 'High Cholesterol', institution = ExcelHomes, doctor = sangeeta, nurse = margaret, practice = practice1, billing = b15)

	print ('--- added 15 patients ---')
	print ('---- adding business information ----')

	r1 = add_entry(amount = 1500, description = 'Checks for January 1', date = datetime.datetime(2015, 1, 1), classification = 'r', practice = practice1)
	r2 = add_entry(amount = 3000, description = 'Checks for January 16', date = datetime.datetime(2015, 1, 16), classification = 'r', practice = practice1)
	r3 = add_entry(amount = 3000, description = 'Checks for February 1', date = datetime.datetime(2015, 2, 1), classification ='r', practice = practice1)
	r4 = add_entry(amount = 1200, description = 'Checks for February 16', date = datetime.datetime(2015, 2, 16), classification = 'r', practice = practice1)

	e1 = add_entry(amount = 150, description = 'Office Expenses', date = datetime.datetime(2015, 1, 1), classification = 'e', practice = practice1)
	e2 = add_entry(amount = 400, description = 'Checks for January 16',date = datetime.datetime(2015, 1, 16), classification= 'e', practice = practice1)
	e3 = add_entry(amount = 900, description = 'Computer Purchase', date = datetime.datetime(2015, 2, 1), classification = 'e', practice = practice1)
	e4 = add_entry(amount = 1000, description = 'Nurse Expense', date = datetime.datetime(2015, 2, 16), classification = 'e', practice = practice1)

	print ('---- added 8 entries ----')
# methods to add to the tables
def add_institution(n, a, inter):
	inst = Institution.objects.create(name = n, address = a, interface = inter)
	return inst

def add_doctor(first, last, addr, practice, email):
	p = Person.objects.create(first_name = first, last_name = last, address = addr)
	d = Doctor.objects.create(person = p, practice = practice, email = email)
	return d

def add_nurse(first, last, addr, practice, email):
	p = Person.objects.create(first_name = first, last_name = last, address = addr)
	n = Nurse.objects.create(person = p, practice = practice, email = email)
	return n

def add_entry(amount, description, date, classification, practice):
	e = Entry.objects.create(amount = amount,description = description, date = date, classification = classification, practice = practice)
	return e

def add_billing(billing_no, plan, company):
	b = Billing.objects.create(insr_plan = plan, insr_number = billing_no, insr_provider = company)
	return b

def add_patient (first, last, address, dob, phone, description, institution, doctor, nurse, practice, billing, notes = "", status = 'Urgent'):
	p = Person.objects.create(first_name = first, last_name = last, address = address)
	patient = Patient.objects.create(person = p, dob =  dob, phone = phone, Notes = notes, 
		description = description, status = status, institution = institution, doctor = doctor, nurse = nurse, practice = practice, billing = billing)
	return patient

def hashPassword(password):
	return hashlib.sha224(password).hexdigest()

# Start execution here!
if __name__ == '__main__':
	print "Starting population script..."
	print datetime.datetime.now()
	django.setup()
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "indmed.settings")
	from polls.models import *
	os.system('python manage.py flush')
	populate()