from django.db import models

#Person object with first name, last name and address field
class Person(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)

#create an individual practice with an associated name
class Practice(models.Model):
	name = models.CharField(max_length = 50)

#Institution is one of the facilities that employs the practice
class Institution(models.Model):
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	interface = models.CharField(max_length = 100)
	practice = models.ForeignKey(Practice)

#Doctor object that refers to the person, practice, and admin
class Doctor(models.Model):
	person = models.OneToOneField(Person)
	practice = models.ForeignKey(Practice)
	email = models.EmailField(max_length = 50)

#Nurse object that referes to people and practices
class Nurse(models.Model):
	person = models.OneToOneField(Person)
	practice = models.ForeignKey(Practice)
	email = models.EmailField(max_length = 50)

#Login object to allow users to log into a particular practice
class LogIn(models.Model):
	person = models.OneToOneField(Person)
	email = models.EmailField(max_length = 50)
	password = models.CharField(max_length = 200)
	practice = models.ForeignKey(Practice)

#Business entries that accord to a practice (either revenue or expenses)
class Entry(models.Model): 
	amount = models.DecimalField(decimal_places = 2, max_digits = 8)
	description = models.CharField(max_length = 100)
	date = models.DateField(blank = True)
	classification = models.CharField(max_length = 20)
	practice = models.ForeignKey(Practice)

#Billing perstains to each individual. Contains plan type, #, and provider
class Billing(models.Model):
	insr_plan = models.CharField(max_length = 100)
	insr_number = models.CharField(max_length = 100)
	insr_provider = models.CharField(max_length = 100)
	
#Patient object with a variety of fields
class Patient(models.Model):
	person = models.ForeignKey(Person)
	dob = models.DateField()
	phone = models.CharField(max_length = 15)
	Notes = models.CharField(max_length = 20)
	description = models.CharField(max_length = 300)
	status = models.CharField(max_length = 100)	
	doctor = models.ForeignKey(Doctor)
	institution = models.ForeignKey(Institution) 
	nurse = models.ForeignKey(Nurse)
	practice = models.ForeignKey(Practice)
	billing = models.ForeignKey(Billing)
