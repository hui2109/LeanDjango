from django.test import TestCase

# Create your tests here.

from .models import Question
from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

q = Question(question_text="Where it is?", pub_date=timezone.now())
q.save()

q = Question(question_text="How to do it?", pub_date=timezone.now())
q.save()

q = Question(question_text="What can I do?", pub_date=timezone.now())
q.save()
