from django.shortcuts import render
import datetime
import json
from reportlab.pdfgen import canvas
import hashlib
# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import *

#Render the home page
def index(request):
	context = {}
	return render(request, 'polls/splash.html', context)

#render the header
def header(request):
	context = {}
	return render(request, 'polls/header.html', context)

#render the footer
def footer(request):
	context = {}
	return render(request, 'polls/footer.html', context)

#render the login page
def login(request):
	context = {}
	return render(request, 'polls/login.html', context)

#render the register page
def register(request):
	context = {}
	return render(request, 'polls/register.html', context)

#render the signup page
def signup(request):
	context = {}
	return render(request, 'polls/signup.html', context)

#view in order to access the page to change passwords or account information
def changeInfo(request):
	#check if session is logged in
	if ('login_id' in request.session):
		p = Person.objects.get(pk = request.session.get('login_id'))
		context = {'log': p}
		return render(request, 'polls/changePass.html', context)
	#return user to main page
	else: 
		request.session.flush()
		request.path = '/'
		return index(request)

#log out of the current session
def logout(request):
	request.session.flush()
	request.path = '/'
	return index(request)

#view of patient management page
def manage(request):
	#check if session is intact
	if ('login_id' in request.session):
		#access all information to populate the page including all patients and institutions and current practice
		p = Person.objects.get(pk = request.session.get('login_id'))
		prac = getCurrentPractice(request)
		#specifies whether the user is a doctor to check how to construct the page
		isDoc = isDoctor(p)
		nurses = Nurse.objects.filter(practice = prac)
		doctors = Doctor.objects.filter(practice = prac)

		#display nurse only page 
		if (isNurse(p)):
			nur = Nurse.objects.get(person = p)
			patients = Patient.objects.filter(practice = prac, nurse = nur)
		else: 
			patients = Patient.objects.filter(practice = prac)

		institutions = Institution.objects.filter(practice = prac)
		context = {'patients': patients, 'nurses': nurses, 'doctors': doctors, 'institutions': institutions, 'log': p, 'prac': prac, 'isDoc': isDoc}
		return render(request, 'polls/manage.html', context)
	else:
		request.session.flush()
		request.path = '/'
		return index(request)

#view of the practice management page
def billing(request):
	#check if the session is active, otherwise return user to home page
	if ('login_id' in request.session):
		p = Person.objects.get(pk = request.session.get('login_id'))
		#gets whether the user is a doctor to know if certain persmissions ought be allowed
		isDoc = isDoctor(p)

		#gets current practice, revenues and expenses and renders the page
		prac = getCurrentPractice(request)
		revenue = Entry.objects.filter(classification='r', practice = prac)
		expenses = Entry.objects.filter(classification='e', practice = prac)
		rsum = 0; 
		esum = 0;
		for r in revenue:
			rsum = rsum + r.amount
		for e in expenses:
			esum = esum + e.amount
		profit = rsum - esum
		nurses = Nurse.objects.filter(practice = prac)
		doctors = Doctor.objects.filter(practice = prac)
		institutions = Institution.objects.filter(practice = prac)
		context = ({'revenue': revenue, 'expenses': expenses, 'rsum': rsum, 'esum': esum, 'profit': profit, 'doctors': doctors, 'nurses':nurses, 'institutions':institutions, 'log': p, 'isDoc': isDoc})
		return render(request, 'polls/billing.html', context)
	else: 
		request.session.flush()
		request.path = '/'
		return index(request)

#auxiliary function in order to create a new patient from a POST request
def createPatient(request):
	if request.method == 'POST':
		#get the relevant information from the post request
		response_data = {}
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		phone = request.POST.get('phone')
		p_status = request.POST.get('status')
		p_doc = request.POST.get('p_doc')
		p_nurse = request.POST.get('p_nurse')
		p_inst = request.POST.get('p_inst')
		p_addr = request.POST.get('p_addr')
		p_desc = request.POST.get('p_desc')

		#insurance information
		p_insr_name = request.POST.get('p_insr_name')
		p_insr_num = request.POST.get('p_insr_no')
		p_insr_provider = request.POST.get('p_insr_provider')
		prac = getCurrentPractice(request)

		#find appropriate person - can abstract away if necessary
		d_pers = get_personid(p_doc)
		n_pers = get_personid(p_nurse)
		#find appropriate nurse and doctor and institution
		patient_doc = Doctor.objects.get(person_id = d_pers.pk)
		patient_nurse = Nurse.objects.get(person_id = n_pers.pk)
		patient_institution = Institution.objects.get(name = p_inst)
		
		#check if the patient exists. If he or she does exist, simply update information. Otherwise create a new patient
		#a patient is deemed to exist if his or her name is already in the database
		if (not personExists(f_name + ' ' + l_name)):
			#create a new person, patient, and billing object to accord with the individual
			p = Person.objects.create(first_name = f_name, last_name = l_name, address = p_addr)
			p.save()
			b = Billing.objects.create(insr_plan = p_insr_name, insr_number = p_insr_num, insr_provider = p_insr_provider)
			b.save()
			pt = Patient(person_id = p.pk, dob = datetime.datetime(1992, 12, 30), phone = phone, description = p_desc, status = p_status, institution = patient_institution, doctor = patient_doc, nurse = patient_nurse, practice = prac, billing = b) 
			pt.save()
		else:
			#Update the information is the patient does already exist
			p = Person.objects.get(first_name = f_name, last_name = l_name)
			pt = Patient.objects.get(person_id = p.pk)
			pt.phone = phone
			pt.status = p_status
			pt.person.address = p_addr
			pt.description = p_desc
			pt.institution = patient_institution
			pt.doctor = patient_doc
			pt.nurse = patient_nurse
			#insurance
			pt.billing.insr_plan = p_insr_name
			pt.billing.insr_number = p_insr_num
			pt.billing.insr_provider = p_insr_provider
			pt.billing.save()
			pt.save()
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

#function to create a new employee: doctor or nurse
def createEmployee(request):
	if request.method == 'POST':
		#get the relevant information from the post request
		response_data = {}
		employee = request.POST.get('emp')
		f_name = request.POST.get('first')
		l_name = request.POST.get('last')
		addr = request.POST.get('address')
		email = request.POST.get('email')
		prac = getCurrentPractice(request)

		#check if the employee already exists
		if (not personExists(f_name + ' ' + l_name)):
			#create a new person and check whether he or she should be a doctor or nurse
			p = Person.objects.create(first_name = f_name, last_name = l_name, address = addr)
			p.save()

			#check if doctor or nurse
			if (employee == 'doctor'):
				dc = Doctor.objects.create(person = p, practice = prac, email = email)
				dc.save()
			elif (employee == 'nurse'):
				ns = Nurse.objects.create(person = p, practice = prac, email = email )
				ns.save()

			#create the login so the user can login with a temporary password

			#hash password


			hashPass = hashPassword('indemed123')
			login = LogIn.objects.create(person = p, email = email, password = hashPass, practice = prac)
			login.save()
			print ('ended the add clause')
		else:
			print ('person / doctor / nurse already exists')
			# **** probably have to modify response data to check success
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

#view to create a new institution
def createInstitution(request):
	if request.method == 'POST':
		#extract the relevant information from the page
		response_data = {}
		prac = getCurrentPractice(request)
		name = request.POST.get('name')
		address = request.POST.get('address')
		interf = request.POST.get('interf')

		#check if the institution already exists
		if (not institutionExists(name)):
			i = Institution.objects.create(name = name, address = address, interface = interf, practice = prac)
			i.save()
		else:
			print ('institution already exists')
			# **** probably have to modify response data to check success
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

#view to create a new entry in the business account
def createEntry(request):
	if request.method == 'POST':
		#extract information from post request and check whether it is revenue or expense
		response_data = {}
		typ = request.POST.get('type')
		if (typ == 'Revenue'):
			typ = 'r'
		elif typ == 'Expense':
			typ = 'e'

		#parse the relevant date and information from the entry
		prac = getCurrentPractice(request)
		desc = request.POST.get('desc')
		date = request.POST.get('date')
		amt = request.POST.get('amt')
		dt_split = date.split('-')
		dt_year =  dt_split[0]
		dt_month = dt_split[1]
		dt_day = dt_split[2]
		dt = datetime.datetime(int(dt_year), int(dt_month), int(dt_day))

		#create new entry and save it
		entry = Entry.objects.create(classification = typ, amount = amt, description = desc, date = dt, practice = prac)
		entry.save()

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

#function to delete a patient
def deletePatient(request):
	if request.method == 'POST':
		#get the relevant data from the post request
		response_data = {}
		first = request.POST.get('f_name')
		last = request.POST.get('l_name')
		name = first + ' ' + last
		pers = get_personid (name)
		patient = Patient.objects.get(person = pers)

		#get the patient and person and delete accordingly
		patient.delete()
		pers.delete()
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)   

#function to create a new practice
def createPractice(request):
	if request.method == 'POST':
		response_data = {}
		#function to extract relevant information from teh apge
		first = request.POST.get('first')
		last = request.POST.get('last')
		practice_name = request.POST.get('practice')
		email = request.POST.get('email')
		address = request.POST.get('address')
		passw = request.POST.get('passw')

		#check whether the practice exists or not based upon the practice name and creator email

		#create a new practice
		if (not checkPracticeCreation(practice_name, email)):
			#create a person, practice, doctor, and login
			p = Person.objects.create(first_name = first, last_name = last, address = address)
			p.save()
			prac = Practice.objects.create(name = practice_name)
			doc = Doctor.objects.create(person = p, practice = prac, email = email)
			doc.save()
			hash_pass = hashPassword(passw)
			login = LogIn.objects.create(person = p, email = email, password = hash_pass, practice = prac)
			login.save()
			#return valid creation 
			response_data['log'] = 'valid'
			request.session['login_id'] = getPerson(username = email, password = passw)
			#move user to the manage page
			manage(request)
		else:
			#creating a new practice failed (already exists or invalid)
			response_data['log'] = 'invalid'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

#function to change the password of a given individual
def changePassword(request):
	if request.method == 'POST':
		#get the relevant information
		response_data = {}
		oldPass = request.POST.get('oldpass')
		newPass1 = request.POST.get('newpass1')
		newPass2 = request.POST.get('newpass2')
		p = Person.objects.get(pk = request.session.get('login_id'))
		login = LogIn.objects.get(person = p)
		
		#check whether the logins confirm, and if the old password matches the one in the database
		if (newPass1 != newPass2): 
			response_data['change'] = 'invalid1'
		elif (hashPassword(oldPass) != login.password):
			response_data['change'] = 'invalid2'
		else: 
			#successfully update the password
			login.password = hashPassword(newPass1)
			login.save()
			response_data['change'] = 'valid'
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

#function to check the login information 
def checkLogin(request):
	if request.method == 'POST':
		response_data = {}
		#get the username and password
		user = request.POST.get('user')
		passw= request.POST.get('passw')

		loggedIn = checkCombo(user, passw)

		#if the combo exists, create a new session and return valid and send the user to the main page
		if (loggedIn):
			response_data['log'] = 'valid'
			request.session['login_id'] = getPerson(username = user, password = passw)
			manage(request)
		else:
			#invalid username and pass. Throw an error message
			print ('invalid username and pass combo')
			print ('invalid for:' +user +' and password ' + passw)
			response_data['log'] = 'invalid'

		return HttpResponse(
			
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

def deleteEntry(request):
	if request.method == 'POST':
		response_data = {}
		#get the username and password
		typ = request.POST.get('type')
		amount = request.POST.get('amount')
		description = request.POST.get('description')
		if (typ == 'Expense'):
			typ = 'e'
		elif (typ == 'Revenue'):
			typ = 'r'

		print ('typ:' +typ)
		entry = Entry.objects.get(classification = typ, amount = amount, description = description)
		entry.delete()

		return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)   

#get a person based upon their first and last name
def get_personid (name):
	personName = name.split(' ')
	first = personName[0]
	last = personName[1]
	pers = Person.objects.get(first_name = first, last_name = last)
	return pers

#checks if a patient exists based on first name and last name. If first name and last name are the same, will assume same person.
def personExists (name):
	personName = name.split(' ')
	first = personName[0]
	last = personName[1]
	return Person.objects.filter(first_name = first, last_name = last).exists()

#check if an institution already exists in the database given its name
def institutionExists(name):
	return Institution.objects.filter(name = name).exists()

#check if a username and password combo already exists
def checkCombo(username, password):
	hash_pass = hashPassword(password)
	return LogIn.objects.filter(email = username, password = hash_pass).exists()

#check if a person exists or not
def getPerson(username, password):
	hash_pass = hashPassword(password)
	p =LogIn.objects.get(email=username, password=hash_pass).person
	return p.pk

#check whether a practice exists
def checkPracticeCreation(name, email):
	b = (Practice.objects.filter(name = name)).exists() or LogIn.objects.filter(email = email)
	return b

#check whether a given person is a doctor
def isDoctor (p):
	b = (Doctor.objects.filter(person = p)).exists()
	return b

#checks whether a given person is a nurse
def isNurse (p):
	return Nurse.objects.filter(person = p).exists()

#gets the practice of an employee. 
def getPractice(p):
	if (isDoctor(p)):
		doc = Doctor.objects.get(person = p)
		return doc.practice
	elif (isNurse(p)):
		nurse = Nurse.objects.get(person = p)
		return nurse.practice

#returns the doctor admin given a practice
def getAdminDoctor(practice):
	return Doctor.objects.get(practice = practice, admin = True)

#gets the current practice for the session
def getCurrentPractice(request):
	p = Person.objects.get(id = request.session['login_id'])
	return getPractice(p)

def hashPassword(password):
	return hashlib.sha224(password).hexdigest()
