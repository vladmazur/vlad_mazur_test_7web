from django.conf.urls import patterns, url

from notesapp import views
from notesapp.views import NotesListAndFormView

urlpatterns = patterns('',
    # url(r'^$', views.index, name='notes'),
    url(r'^$', NotesListAndFormView.as_view(), name='notes-list'),
)