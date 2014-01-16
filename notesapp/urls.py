from django.conf.urls import patterns, url

from notesapp import views

urlpatterns = patterns('',
    url(r'^notes', views.index, name='notes')
)