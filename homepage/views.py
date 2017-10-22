from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import resolve
import datetime

from .models import CheckList
from .models import Question
from .models import Option
from .models import Answer
from.models import ChecklistAnswer

from .CustomClasses.ChecklistLocal import ChecklistLocal
from .CustomClasses.QuestionLocal import QuestionLocal
from .CustomClasses.OptionLocal import OptionLocal

class IndexView(generic.ListView):

    model = None
    template_name = 'homepage/index.html'

    id = 0
    context_object_name = 'query_set'

    def get_queryset(self):

        return ["Er du GDPR COMPLIANT?", [fetchStartChecklist()]]

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

class ConfirmationView(generic.ListView):

    model = None
    template_name = 'homepage/confirmation.html'
    id = 4
    context_object_name = 'query_set'

    def get_queryset(self):

        return ['Takk for ditt svar']


def fetchStartChecklist():

    return createAndReturnChecklist(CheckList.objects.get(is_front=True))


def createAndReturnChecklist(checklistK):

    checklist_1 = ChecklistLocal(checklistK.name, checklistK.pk, checklistK.is_front)

    for questionK in Question.objects.filter(checkList__pk=checklistK.pk):

        new_question = QuestionLocal(questionK.question_text, questionK.isOptions, questionK.pk)
        number_options = Option.objects.filter(question__pk=questionK.pk).count()

        if number_options > 0:
            new_question.setIsOptions(True)

        if questionK.isOptions and new_question.getIsOptions():

            for option in Option.objects.filter(question__pk=questionK.pk, question__isOptions=questionK.isOptions):
                new_option = OptionLocal(option.optionText, option.pk)
                new_question.addOption(new_option)

        checklist_1.addQuestion(new_question)

    return checklist_1


def fetchCheckLists():

    all_checklists = []

    for checklistK in CheckList.objects.filter(is_front=False):

        all_checklists.append(createAndReturnChecklist(checklistK))

    return all_checklists


def sendInChecklist(request):

    checklist_id = request.POST['checklist-id']
    is_front = request.POST['is_front']
    email = request.POST['email_sender']
    is_filled = True

    answer_checklist = ChecklistAnswer(answer_email=email, checklist=CheckList.objects.get(pk=str(checklist_id)))
    answer_checklist.save()
    for question in Question.objects.filter(checkList__pk=checklist_id):

        if question.isOptions:
            answer = request.POST['answer-option-' + checklist_id + '-' + str(question.id)]
        else:
            answer = request.POST['answer-' + checklist_id + '-' + str(question.id)]

        if answer == "":
            is_filled = False

        db_answer = Answer(answerText=answer, question=question, answerChecklist=answer_checklist)
        db_answer.save()

    if not is_filled:
        ChecklistAnswer.objects.get(answer_email=email).delete()


    return redirect('homepage:confirmation', email)


