from django.db import models
from django.forms import ModelForm
from django import forms
# from django.utils import timezone
import datetime

# class Tag(models.Model):
# 	tag_name = 		models.CharField(max_length=35)
# 	created_at  = 	models.DateTimeField('date created')

# 	def __unicode__(self):
# 		return self.tag_name

class Author(models.Model):
    name = 	models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__ (self):
    	return self.name

class Note(models.Model):
    title = 	models.CharField(max_length=200)
    text = 		models.TextField()
    pub_date = 	models.DateTimeField('date published', default=datetime.datetime.now)
    author = 	models.ForeignKey(Author, blank=True, null=True)
    # tags = 		models.ManyToManyField(Tag, related_name='notes')

    def __unicode__ (self):
    	return self.title

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'author']

    title = forms.CharField(max_length=200, min_length=4)