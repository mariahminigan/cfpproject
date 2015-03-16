from django.contrib import admin
from .models import Question, Comment
# Registering my models in the app. 

admin.site.register(Question)
admin.site.register(Comment)
