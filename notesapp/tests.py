# -*- coding: utf-8 -*-

import datetime

from django.utils import timezone
from django.test import TestCase, RequestFactory
from views import NotesListAndFormView

# from django.core.urlresolvers import reverse

from notesapp.models import Note, Author

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
	# Убрал это из тестов, потому что по условию данные должны быть
	# (fixtures), но тогда тест проваливается

    # def test_index_view_with_no_notes(self):
    #     """
    #     If no notes exist, an appropriate message should be displayed.
    #     """
    #     response = self.client.get('/notes/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "No notes are available")
    #     self.assertQuerysetEqual(response.context['latest_notes_list'], [])

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        request = self.factory.get('/notes/')
        # additional params can go after request
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view_with_a_past_note(self):
        """
        Notes with a pub_date in the past should be displayed on the index page.
        """
        n1 = Note.objects.get(id=1)
        n2 = create_note(title="Past note", days= -10)

        request = self.factory.get('/notes/')
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        context = response.context_data
        self.assertEqual(context['note_list'][0], n1)
        self.assertEqual(context['note_list'][1], n2)

    def test_index_view_with_a_future_note(self):
        """
        Notes with a pub_date in the past should be displayed on the index page.
        """
        n1 = Note.objects.get(id=1)
        n2 = create_note(title="Future note", days= 10)

        request = self.factory.get('/notes/')
        response = NotesListAndFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        context = response.context_data

        self.assertEqual(context['note_list'][0], n1)
        self.assertEqual(context['note_list'][1], n2)
