from django.db import models

class Tag(models.Model):
	tag_name = 		models.CharField(max_length=35)
	created_at  = 	models.DateTimeField('date created')

	def __unicode__(self):
		return self.tag_name

class Author(models.Model):
    name = 	models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__ (self):
    	return self.name

class Note(models.Model):
    title = 	models.CharField(max_length=200)
    text = 		models.TextField()
    pub_date = 	models.DateTimeField('date published')
    author = 	models.ForeignKey(Author, blank=True, null=True)
    # tags = 		models.ManyToManyField(Tag, related_name='notes')

    def __unicode__ (self):
    	return self.title