from django.contrib import admin

# Register your models here.
from notesapp.models import Author, Note, Tag

# class NoteAdmin(admin.ModelAdmin):
#     fields = ['title', 'pub_date', 'author']

admin.site.register(Author)
admin.site.register(Note)
admin.site.register(Tag)