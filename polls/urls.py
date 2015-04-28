from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^', views.index, name='polls'),	#this maps to the polls page
)