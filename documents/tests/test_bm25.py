from django.test import TestCase
from documents.models import Document, Question
from documents.utils.bm25_search import find_relevant_documents_bm25
from datetime import date

class BM25SearchTest(TestCase):
    def setUp(self):
        self.doc = Document.objects.create(
            title="Test Doc",
            text="This document explains Django and BM25.",
            date=date.today()
        )
        self.question = Question.objects.create(question_text="What is BM25?")
        self.question.documents.add(self.doc)

    def test_bm25_returns_expected_dict(self):
        results = find_relevant_documents_bm25(self.question)
        self.assertGreaterEqual(len(results), 1)
        self.assertIn("title", results[0])
        self.assertIn("score", results[0])
        titles = [r["title"] for r in results]
        self.assertIn("Test Doc", titles)
