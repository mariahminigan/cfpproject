#All urls besides the /admin/ url will redirect here from cfpsite/urls.py

from django.conf.urls import patterns, include, url
from . import views #Importing all the views used in the questionblog app. 

urlpatterns = patterns('', #This is an empty string, not a string with a space in it! 
	url(r'^$', views.question_list), #This assigns the question_list view to the home URL. 
	#Django starts looking for a url pattern at ^ and stops at $, so '^$' is asking it to look for an empty string. 
	#This means that the question_list view is where it will direct anyone going to the main site url. 
	url(r'^question/(?P<pk>[0-9]+)/$', views.question_comments), #This is telling Django how the URL should read. It says that after the beginning ^, the
	#URL should read question/. Then it takes everything placed after that and transfers it to a view
	#called pk, which is what I'm calling my primary keys. [0-9] means that next, we need some digits (not letters). And the + sign means
	#that there can be more than one digit there. In each url, this digit is the pk of one of my questions. Then another /, then $ for the end.  
	#The idea is that if the URL I type is http://127.0.0.1:8000/post/3/, Django knows I am looking
	#for a view called question_comments. Then it uses the number 3 to get information about that view.
)
