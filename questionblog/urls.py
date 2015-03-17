#All urls besides the /admin/ url will redirect here from cfpsite/urls.py

from django.conf.urls import patterns, include, url
#Importing all the views used in the questionblog app. 
from . import views 

#This is an empty string, not a string with a space in it!
urlpatterns = patterns('', 
	#This assigns the question_list view to the home URL. 
	#Django starts looking for a url pattern at ^ and stops at $,
	# so '^$' is asking it to look for an empty string. 
	#This means that the question_list view is where it will 
	# direct anyone going to the main site url. 
	url(r'^$', views.question_list),
	#This is telling Django how the URL should read. 
	#It says that after the beginning ^, the URL should read question/. 
	#Everything placed after that is a pk, which is what I'm calling my primary keys. 
	#Primary keys are nuique identifiers of items in the database.
	#[0-9] means that next, we need some digits (not letters). 
	#And the + sign means that there can be more than one digit there. 
	#In each url, this digit is the pk of one of my questions. 
	#Then another /, then $ for the end.  
	#The idea is that if the URL I type is http://127.0.0.1:8000/question/3/, 
	#Django knows I am looking for a view called question_comments. 
	#Then it uses the pk, 3, to get information about that view.
	url(r'^question/(?P<pk>[0-9]+)/$', views.question_comments), 
)
