from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import resolve
import datetime

from .models import CheckList
from .models import Question
from .models import Option

from .CustomClasses.ChecklistLocal import ChecklistLocal
from .CustomClasses.QuestionLocal import QuestionLocal

class IndexView(generic.ListView):

    model = None
    template_name = 'homepage/index.html'

    id = 0
    context_object_name = 'query_set'

    def get_queryset(self):

        return ["Er du GDPR COMPLIANT?"]

class AboutView(generic.ListView):

    model = None

    template_name = 'homepage/about.html'
    id = 1
    context_object_name = 'query_set'

    def get_queryset(self):

        return ["Om oss"]


class AboutGDPRView(generic.ListView):

    model = None
    template_name = 'homepage/aboutGDPR.html'
    id = 2
    context_object_name = 'query_set'

    def get_queryset(self):

        return ["Om GDPR"]

class ChecklistView(generic.ListView):

    model = None
    template_name = 'homepage/checklists.html'
    id = 3
    context_object_name = 'query_set'

    def get_queryset(self):

        return ["Sjekklister", fetchCheckLists()]


def fetchCheckLists():

    all_checklists = []

    for checklistK in CheckList.objects.all():

        checklist_1 = ChecklistLocal(checklistK.name, checklistK.pk)

        for questionK in Question.objects.filter(checkList__pk=checklistK.pk):

            newQuestion = QuestionLocal(questionK.question_text, questionK.isOptions)

            if questionK.isOptions:

                for option in Option.objects.filter(question__pk=questionK.pk, question__isOptions=questionK.isOptions):

                    newQuestion.addOption(option.optionText)

            checklist_1.addQuestion(newQuestion)




        all_checklists.append(checklist_1)


    return all_checklists


