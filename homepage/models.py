from django.db import models

# Create your models here.

class CheckList(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):

        return self.name

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    checkList = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    isOptions = models.BooleanField(default=True)

    def __str__(self):

        return self.question_text


class Option(models.Model):

    optionText = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):

        return self.optionText


class OptionAnswer(models.Model):

    answer = models.ForeignKey(Option) ## No CASCADE, do not want to delete answer if option is deleted

    def __str__(self):

        return self.answer.optionText

class FreeAnswer(models.Model):

    answerText = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):

        return self.answerText




