# -*- coding: utf-8 -*-

import datetime

from django.utils import timezone
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from hellodjango.apps.notesapp.views import NotesListAndFormView
from hellodjango.apps.notesapp.models import Note, Author

def create_author(name):
	return Author(name = name, email = "dow@gmail.com")

def create_note(title, days):
    """
    Creates a note with the given `title` published the given number of
    `days` offset to now (negative for polls published in the past,
    positive for polls that have yet to be published).
    """
    return Note.objects.create(title=title, text = "text", 
        pub_date=timezone.now() + datetime.timedelta(days=days))

class NoteViewTests(TestCase):
    def setUp(self):
        """
        Delete all objects from fixtures just before testing
        """
        self.factory = RequestFactory()
        Author.objects.all().delete()


    def test_index_view_with_no_notes(self):
        """
        If no notes exist, an appropriate message should be displayed.
        """
        request = self.factory.get(reverse('notes-list'))
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No notes are available")
        self.assertQuerysetEqual(list(response.context_data['note_list']), [])

    def test_list_view(self):
        """
        Test for 200 ok code
        """
        request = self.factory.get(reverse('notes-list'))
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view_with_a_past_note(self):
        """
        Notes with a pub_date in the past should be displayed on the index page.
        """
        n = create_note(title="Past note", days= -10)

        request = self.factory.get(reverse('notes-list'))
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        context = response.context_data
        self.assertEqual(list(context['note_list']), [n])

    def test_index_view_with_a_future_note(self):
        """
        Notes with a pub_date in the past should be displayed on the index page, 
        but no future notes
        """
        n = create_note(title="Future note", days= 10)

        request = self.factory.get(reverse('notes-list'))
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        context = response.context_data

        self.assertEqual(list(context['note_list']), [n])
