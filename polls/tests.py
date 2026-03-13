from urllib.request import urlopen

from django.test import TestCase, SimpleTestCase, TransactionTestCase, LiveServerTestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionTestCase(TestCase):

    def test_question_creation(self):
        question = Question.objects.create(
            question_text="Test Question",
            pub_date=timezone.now()
        )
        self.assertEqual(question.question_text, "Test Question")

    def test_question_exists_in_database(self):
        Question.objects.create(
            question_text="Another Question",
            pub_date=timezone.now()
        )
        self.assertEqual(Question.objects.count(), 1)


class URLTest(SimpleTestCase):

    def test_index_url(self):
        url = reverse("polls:index")
        self.assertEqual(url, "/polls/")


class QuestionTransactionTest(TransactionTestCase):

    def test_database_transaction(self):
        Question.objects.create(
            question_text="Transaction Question",
            pub_date=timezone.now()
        )
        self.assertEqual(Question.objects.count(), 1)


class PollsLiveServerTest(LiveServerTestCase):

    def test_server_response(self):
        response = urlopen(self.live_server_url + "/polls/")
        self.assertEqual(response.getcode(), 200)