from django.contrib import admin

# Register your models here.
from notesapp.models import Author, Note, Tag

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'author__name']

admin.site.register(Author)
admin.site.register(Note, NoteAdmin)
admin.site.register(Tag)