# -*- coding: utf-8 -*-

import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from notesapp.models import Note, Author, Tag

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

    def test_index_view_with_a_past_note(self):
        """
        Notes with a pub_date in the past should be displayed on the index page.
        """
        create_note(title="Past note", days= -10)
        response = self.client.get('/notes/')
        self.assertQuerysetEqual(
            response.context['latest_notes_list'],
            ['<Note: add>', '<Note: title>', '<Note: Past note>']
        )

    def test_index_view_with_a_future_note(self):
        """
        Notes with a pub_date in the past should be displayed on the index page.
        """
        create_note(title="Future note", days= 10)
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_notes_list'], ['<Note: add>', '<Note: title>'])
        # self.assertContains(response, "No notes are available")
        # несколько нотов из fixtures будут видны