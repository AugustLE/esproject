from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import resolve
import datetime

from .models import CheckList
from .models import Question
from .models import Option

from .CustomClasses.ChecklistLocal import ChecklistLocal
from .CustomClasses.QuestionLocal import QuestionLocal
from .CustomClasses.OptionLocal import OptionLocal

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

            newQuestion = QuestionLocal(questionK.question_text, questionK.isOptions, questionK.pk)
            number_options = Option.objects.filter(question__pk=questionK.pk).count()

            if number_options > 0:
                newQuestion.setIsOptions(True)

            if questionK.isOptions and newQuestion.getIsOptions():

                for option in Option.objects.filter(question__pk=questionK.pk, question__isOptions=questionK.isOptions):

                    newOption = OptionLocal(option.optionText, option.pk)
                    newQuestion.addOption(newOption)

            checklist_1.addQuestion(newQuestion)

        all_checklists.append(checklist_1)

    return all_checklists


def sendInChecklist(request):

    checklist_id = request.POST['checklist-id']

    for question in Question.objects.filter(checkList__pk=checklist_id):

        if question.isOptions:

            answer = request.POST['answer-option-' + checklist_id + '-' + str(question.id)]
            print(answer)

        else:
            answer = request.POST['answer-' + checklist_id + '-' + str(question.id)]

            print(answer)

    return redirect('homepage:checklists')