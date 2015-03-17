from django.shortcuts import render
#Imports Question and Comment models so I can get Questions and Comments in the views. 
from .models import Question, Comment 
#This means that instead of getting a weird error when you try to 
# find a question that doesn't exist (like question 231), you'll just get a 404 page.
from django.shortcuts import render, get_object_or_404 
#Imports my CommentForm.
from .forms import CommentForm 
#Will let me go immediately refresh the page after creating a new comment.  
from django.shortcuts import redirect 

#Creating a method called question_list that takes a request 
# and puts info together in my template, question_list.html. 
def question_list(request): 
	#Makes questions a variable containing the QuerySet that finds all my Questions. 
	questions = Question.objects.all() 
	#Stuff between the {} is what will be used in the template. 
	#Template is located at questionblog/question_list.html.
	return render(request, 'questionblog/question_list.html', {'questions':questions}) 

#This will create a view that displays an individual question with its comments. 
#pk identifies which question you're looking for--each one has a unique pk. 
def question_comments(request, pk):
	#Creates a variable for the Question, or else gives a 404 error if
	# no question exists with the given pk. 
	question = get_object_or_404(Question, pk=pk) 
	#Creates a variable for the comments associated with each question 
	# by finding only the comments attached to a given pk. 
	comments = Comment.objects.filter(question=pk) 
	#If someone hits the save button to actually post a comment in this view, 
	# rather than just GETting the questions and comments associated 
	# with this pk, the form does the following:
	if request.method == "POST": 
		#Creates a variable containing the information entered in the form
		form =  CommentForm(request.POST)
		#Makes sure there's something in the text field.
		if form.is_valid(): 
			#Saves the contents of the form. Doesn't commit it to database. 
			comment = form.save(commit=False) 
			#Makes the question associated with this comment equal to 
			# the question variable defined above.
			comment.question = question  
			#Saves the contents of the form, with the associated question, as a new comment.
			comment.save()  
		return redirect('questionblog.views.question_comments', pk=pk)
	#If no one is trying to post a comment while in this view, 
	# then the form is just chilling on the page.
	else: 
		#Creates a variable for the CommentForm that will be in this view. 
		#There's a lovely blank box at the bottom of the page. 
		form = CommentForm() 
	#Compiles all the variables defined above, sends them to question_comments.html, the template file. 
	#That template will be filled with the questions called up, the associated comments, and the comment form. 
	return render(request, 'questionblog/question_comments.html', {'question' : question, 'comments' : comments, 'form': form})  
