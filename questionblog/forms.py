#Importing forms!
from django import forms  
#Importing the Comment model, to be used with forms! 
from .models import Comment 

#CommentForm is the name of the form. Then, with forms.ModelForm 
# I'm telling Django that this is a ModelForm--it knows what that means. 
#ModelForm is a specific type of form that Django has, 
# and there are others you can use for different stuff. 
class CommentForm(forms.ModelForm): 
	# Tells Django which model should be used to create the CommentForm. 
	#In this case, the Comment model. 
	class Meta: 
		model = Comment
		#This is where I tell Django which fields should end up in the form. 
		#created_date will be set automatically--there's no need to have it on the form. 
		#Don't forget the comma after 'text'!
		fields = ('text',) 
		#Removing the "Text:" label from the add comment box. 
		labels = {
			'text': '',
		}