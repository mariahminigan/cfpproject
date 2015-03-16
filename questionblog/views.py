from django.shortcuts import render
from .models import Question, Comment #Imports Question and Comment models so I can get Questions and Comments in the views. 
from django.shortcuts import render, get_object_or_404 #This means that instead of getting a weird error when you try to find a question that doesn't 
#exist (like question 231), you'll just get a 404 page.

def question_list(request): #Creating a method called question_list that takes a request and puts things together in my template, question_list.html. 
	questions = Question.objects.all() #This is now a variable containing the QuerySet that finds all my Questions. 
	return render(request, 'questionblog/question_list.html', {'questions':questions}) #Stuff between the {} is what will be used in the template. 


def question_comments(request, pk): #This will create a view that displays an individual question with its comments. 
#pk identifies which question you're looking for.
	question = get_object_or_404(Question, pk=pk) #Creates a variable for the Question, or else gives a 404 error.
	#qustion_comments.html is the template file. That template will be filled with the Questions called up, and the associated comments. 
	comments = Comment.objects.filter(question=pk)
	return render(request, 'questionblog/question_comments.html', {'question' : question, 'comments' : comments})
