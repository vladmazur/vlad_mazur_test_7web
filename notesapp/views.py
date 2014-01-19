from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin, ModelFormMixin

from notesapp.models import Note, NoteForm

# def index(request):
#     latest_notes_list = Note.objects.filter(
#     	pub_date__lte=timezone.now()
#     	).order_by('-pub_date')
#     context = {
#         'latest_notes_list': latest_notes_list}

#     return render(request, 'notes/index.html', context)

class NotesListAndFormView(ListView, FormMixin):

    form_class = NoteForm
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NotesListAndFormView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        context['form'] = self.form # Just include the form

        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.form.save()
            self.form = NoteForm()

        return ListView.get(self, request, *args, **kwargs)
