from django import forms #Importing forms! 
from .models import Comment #Importing the Comment model, to be used with forms! 

class CommentForm(forms.ModelForm): #CommentForm is the name of the form. Then, with forms.ModelForm I'm telling Django that this is a ModelForm--it knows what that means. 
#ModelForm is a specific type of form that Django has, and there are others you can use for different stuff. 

	class Meta: # Tells Django which model should be used to create the CommentForm. In this case, the Comment model. 
		model = Comment
		fields = ('text',) #This is where I tell Django which fields should end up in the form. created_date will be set automatically--there's no need to have it on the form. 
		#Don't forget the comma after 'text'!