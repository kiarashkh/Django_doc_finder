from django.test import TestCase
from documents.models import Document, Question
from documents.utils import llm_answer
from datetime import date

class LLMAnswerTest(TestCase):
    def setUp(self):
        self.doc = Document.objects.create(
            title="LLM Doc",
            text="LangChain is used for chaining prompts.",
            date=date.today()
        )
        self.question = Question.objects.create(question_text="How does LangChain work?")
        self.question.documents.add(self.doc)

    def test_llm_pipeline_updates_answer(self):
        output = llm_answer.answer_question_with_llm(self.question)
        self.assertIsInstance(output, str)
        self.question.refresh_from_db()
        self.assertEqual(self.question.answer_text, output)
