from django.shortcuts import render
from .models import Question, Comment #Imports Question and Comment models so I can get Questions and Comments in the views. 
from django.shortcuts import render, get_object_or_404 #This means that instead of getting a weird error when you try to find a question that doesn't 
#exist (like question 231), you'll just get a 404 page.
from .forms import CommentForm #Imports my CommentForm.
from django.shortcuts import redirect #Will let me go immediately refresh the page after creating a new comment.  

def question_list(request): #Creating a method called question_list that takes a request and puts things together in my template, question_list.html. 
	questions = Question.objects.all() #This is now a variable containing the QuerySet that finds all my Questions. 
	return render(request, 'questionblog/question_list.html', {'questions':questions}) #Stuff between the {} is what will be used in the template. 


def question_comments(request, pk): #This will create a view that displays an individual question with its comments. 
#pk identifies which question you're looking for--each one has a unique pk. 
	question = get_object_or_404(Question, pk=pk) #Creates a variable for the Question, or else gives a 404 error.
	#qustion_comments.html is the template file. That template will be filled with the Questions called up, and the associated comments. 
	comments = Comment.objects.filter(question=pk) #Creates a variable for the comments associated with each question by finding only the comments attached to a given pk. 
	if request.method == "POST": #If someone tries to post a comment in this view...
		form =  CommentForm(request.POST) #Constructs the form with data from the form. instance = comment associates the new comment with the question being accessed. 
		if form.is_valid(): #Makes sure there's something in the text field.
			comment = form.save(commit=False) #Saving the contents of the form. Doesn't commit it to database. 
			comment.question = question #Makes the question associated with this comment equal to the question variable defined above. 
			comment.save() #Saves the contents of the form, with the associated question, as a new comment. 
		return redirect('questionblog.views.question_comments', pk=pk)
	else: #If no one is trying to post a comment while in this view, and it's just chilling on the page.
		form = CommentForm() #Creates a variable for the CommentForm that will be in this view. There's a lovely blank box at the bottom of the page. 
	return render(request, 'questionblog/question_comments.html', {'question' : question, 'comments' : comments, 'form': form}) #Compiles all the info listed above, sends it to my template for this view. 
