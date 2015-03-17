from django.db import models
from django.utils import timezone

#Creating two models: Question and Comment.
#Questions have only text as an attribute, plus an identifying primary key
# (which Django takes care of, it'll be question_id or comment_id, respectively). 
#That pk is how Comments can be connected to them. 
#Comments have several attributes: text, created_date, and the Question they're answering.
#Questions are an attribute of comments because each comment answers only one question, 
# but each question can have many comments. 

#Use class to define an object. (models.Model) tells Django to save the Question in the database. 
class Question(models.Model): 
	#CharField is for a field with a limited number of characters. 
	#Titles didn't actually end up being necessary here, but I thought
	#about using them on the main page to identify questions. 
	title = models.CharField(max_length=200) 
	#TextField() is for long text without a character limit.
	text = models.TextField()  

class Comment(models.Model):
	text = models.TextField()
	#This attribute is a date and time using the current time in my timezone. 
	#You don't specify a created date/time when posting--
	# it defaults to the current date/time.
	created_date = models.DateTimeField(default=timezone.now)
	#Each comment has, as an attribute, the primary key of one of the Questions. 
	#ForeignKey is how Django finds that pk.    
	question = models.ForeignKey('Question') 

