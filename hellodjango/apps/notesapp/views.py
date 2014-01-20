from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin, ModelFormMixin

from hellodjango.apps.notesapp.models import Note, NoteForm

class NotesListAndFormView(ListView, FormMixin):
    '''
    Implement CBV for main page, where list if of notes 
    and new note form are placed
    '''
    form_class = NoteForm
    model = Note

    def get_context_data(self, **kwargs):
        """
        Add form to view
        """
        context = super(NotesListAndFormView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        context['form'] = self.form # Just include the form

        return context

    def get(self, request, *args, **kwargs):
        """
        Goes here when loading page
        """
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Save form data if valid; 
        return empty form if valid or old form with error if not
        """
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.form.save()
            self.form = NoteForm()

        return ListView.get(self, request, *args, **kwargs)

my_f = NotesListAndFormView.as_view()
