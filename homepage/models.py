from django.db import models
from datetime import datetime
from django.utils import timezone

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from user.models import CustomUser


class CheckList(models.Model):

    name = models.CharField(max_length=100)
    is_front = models.BooleanField(default=False)

    def __str__(self):

        return self.name

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    checkList = models.ForeignKey(CheckList, on_delete=models.CASCADE, related_name='questions')
    isOptions = models.BooleanField(default=True)
    priority = models.CharField(max_length=3, unique=False, default='0')

    def __str__(self):

        return self.question_text


class Option(models.Model):

    optionText = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    solution = models.CharField(max_length=500, blank=True)

    def __str__(self):

        return self.optionText

class ChecklistAnswer(models.Model):

    answer_email = models.EmailField(max_length=200)
    checklist = models.ForeignKey(CheckList)
    date_sent = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(CustomUser, related_name='checklistAnswers', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.answer_email + " - " + self.checklist.name



class Answer(models.Model):

    answerText = models.CharField(max_length=500)
    question = models.CharField(max_length=500)
    answerChecklist = models.ForeignKey(ChecklistAnswer, on_delete=models.CASCADE, related_name='answers')
    option = models.ForeignKey(Option, blank=True, null=True)

    def __str__(self):
        return self.answerText






