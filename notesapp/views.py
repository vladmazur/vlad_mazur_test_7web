from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from notesapp.models import Note

def index(request):
    latest_notes_list = Note.objects.filter(
    	pub_date__lte=timezone.now()
    	).order_by('-pub_date')
    context = {
        'latest_notes_list': latest_notes_list}
    return render(request, 'notes/index.html', context)