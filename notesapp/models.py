from django.db import models

class Author(models.Model):
    # poll = models.ForeignKey(Poll)
    name = models.CharField(max_length=200)
    notes_count = models.IntegerField(default=0)

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author)