from django.conf.urls import patterns, url

from notesapp import views
from notesapp.views import NotesListView

urlpatterns = patterns('',
    # url(r'^$', views.index, name='notes'),
    url(r'^$', NotesListView.as_view(), name='notes-list'),
)