from django.conf.urls import patterns, url

from hellodjango.apps.notesapp.views import NotesListAndFormView

urlpatterns = patterns('',
    url(r'^$', NotesListAndFormView.as_view(), name='notes-list'),
)