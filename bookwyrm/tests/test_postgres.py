""" django configuration of postgres  """
from django.test import TestCase

from bookwyrm import models


class PostgresTriggers(TestCase):
    """special migrations, fancy stuff ya know"""

    def test_search_vector_on_create(self):
        """make sure that search_vector is being set correctly on create"""
        book = models.Edition.objects.create(title="The Long Goodbye")
        book.refresh_from_db()
        self.assertEqual(book.search_vector, "'goodby':3A 'long':2A")

    def test_search_vector_on_update(self):
        """make sure that search_vector is being set correctly on edit"""
        book = models.Edition.objects.create(title="The Long Goodbye")
        book.title = "The Even Longer Goodbye"
        book.save(broadcast=False)
        book.refresh_from_db()
        self.assertEqual(book.search_vector, "'even':2A 'goodby':4A 'longer':3A")

    def test_search_vector_fields(self):
        """use multiple fields to create search vector"""
        author = models.Author.objects.create(name="The Rays")
        book = models.Edition.objects.create(
            title="The Long Goodbye",
            subtitle="wow cool",
            series="series name",
            languages=["irrelevent"],
        )
        book.authors.add(author)
        book.refresh_from_db()
        self.assertEqual(
            book.search_vector,
            "'cool':5B 'goodby':3A 'long':2A 'name':9 'rays':7B 'seri':8 'the':6B 'wow':4B",
        )

    def test_seach_vector_on_author_update(self):
        """update search when an author name changes"""
        author = models.Author.objects.create(name="The Rays")
        book = models.Edition.objects.create(
            title="The Long Goodbye",
        )
        book.authors.add(author)
        author.name = "Jeremy"
        author.save(broadcast=False)
        book.refresh_from_db()

        self.assertEqual(book.search_vector, "'goodby':3A 'jeremy':4B 'long':2A")

    def test_seach_vector_on_author_delete(self):
        """update search when an author name changes"""
        author = models.Author.objects.create(name="Jeremy")
        book = models.Edition.objects.create(
            title="The Long Goodbye",
        )

        book.authors.add(author)
        book.refresh_from_db()
        self.assertEqual(book.search_vector, "'goodby':3A 'jeremy':4B 'long':2A")

        book.authors.remove(author)
        book.refresh_from_db()
        self.assertEqual(book.search_vector, "'goodby':3A 'long':2A")

    def test_search_vector_stop_word_fallback(self):
        """use a fallback when removing stop words leads to an empty vector"""
        book = models.Edition.objects.create(
            title="there there",
        )
        book.refresh_from_db()
        self.assertEqual(book.search_vector, "'there':1A,2A")
