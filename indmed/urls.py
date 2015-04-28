from django.conf.urls import patterns, include, url
from django.contrib import admin

#Check the URL request against the patterns 
urlpatterns = patterns('',
	(r'^create_patient/', 'polls.views.createPatient'),
	(r'^delete_patient/', 'polls.views.deletePatient'),
	(r'^generate_report/', 'polls.views.generateReport'),
	(r'^create_entry/', 'polls.views.createEntry'),
	(r'^create_employee/', 'polls.views.createEmployee'),
	(r'^delete_entry/', 'polls.views.deleteEntry'),
	(r'^create_practice/', 'polls.views.createPractice'),
	(r'^check_login/', 'polls.views.checkLogin'),
	(r'^change_password/', 'polls.views.changePassword'),
	(r'^create_institution/', 'polls.views.createInstitution'),
	(r'^create_employee/', 'polls.views.createEmployee'),
	(r'^polls/templates/header.html', 'polls.views.header'),
	(r'^polls/templates/footer.html', 'polls.views.footer'),
	(r'^polls/templates/login.html', 'polls.views.login'),
	(r'^polls/templates/signup.html', 'polls.views.signup'),
	(r'^polls/templates/dashboard.html', 'polls.views.dashboard'),
	(r'^polls/templates/business.html', 'polls.views.business'),
	(r'^register$', 'polls.views.register'),
	(r'^manage$', 'polls.views.manage'),
	(r'^billing$', 'polls.views.billing'),
	(r'^changeInfo$', 'polls.views.changeInfo'),
	(r'^logout$', 'polls.views.logout'),
    url(r'^$', 'polls.views.index'),  
	url(r'^', include('polls.urls')),  	#this is an arbitrary sequence that is being matched against
    url(r'^admin/', include(admin.site.urls)),
)
