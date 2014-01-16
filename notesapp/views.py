from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext, loader

from notesapp.models import Note

def index(request):
    latest_notes_list = Note.objects.order_by('pub_date')[:5]
    context = {
        'latest_notes_list': latest_notes_list}
    return render(request, 'notes/index.html', context)