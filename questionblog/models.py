from django.db import models
from django.utils import timezone

#Creating two models: Question and Comment.
#Questions have only text as an attribute, plus an identifying primary key (which Django takes care of, it'll be question_id or comment_id, respectively). That pk is how Comments can be connected to them. 
#Comments have several attributes: text, created_date, the Question they're answering, and the ability to be published. 
#Questions are an attribute of comments because each comment answers only one question, but each question can have many comments. 

class Question(models.Model): #Use class to define an object. (models.Model) tells Django to save the Question in the database. 
	title = models.CharField(max_length=200) #CharField is for a field with a limited number of characters. The title here is mostly for use in the admin section and doesn't appear to the user. 
	text = models.TextField() #TextField() is for long text without a character limit. 

class Comment(models.Model):
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now) #This attribute is a date and time using the current time in my timezone. You don't specify a created date/time when posting--it defaults to the current date/time. 
	question = models.ForeignKey('Question') #Each comment has, as an attribute, the primary key of one of the Questions. ForeignKey is how Django finds that pk.  

	# def publish(self): #This is a function that is an attribute of each comment. Each comment can be published
	# 	self.published_date = timezone.now()
 #        self.save()
 #Took this bit out because there isn't actually a published_date here. Could just replace created_date with that. 
