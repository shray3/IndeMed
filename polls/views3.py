from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import *



#just trying to get all the people
def index(request):
	context = {}
	print ('in index')
	return render(request, 'polls/csstemplate.html', context)

def header(request):
	context = {}
	return render(request, 'polls/header.html', context)

def footer(request):
	context = {}
	return render(request, 'polls/footer.html', context)

def splash(request):	
	context = {}
	print 'going into splash'
	return render(request, 'polls/csstemplate.html', context)

#making the log-in page
# def login(request):
# 	context = {}
# 	print 'hey im in the login page'
# 	return render(request, 'polls/login.html', context)

# def manage(request):
# 	context = {}
# 	print 'hey im in the manage page'
# 	return render(request, 'polls/manage.html', context)

# def billing(request):
# 	context = {}
# 	print '** billing page **'
# 	return render(request, 'polls/billing.html', context)


