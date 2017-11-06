from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.urlresolvers import resolve
import datetime
from .forms import UserLoginForm, UserSignupForm

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


class UserLoginFormView(View):

    form_class = UserLoginForm
    template_name = 'homepage/login.html'
    id = 5
    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'view_id': 5})


    #process form data
    #loggs in the user
    def post(self, request):

        email = request.POST['email']
        password = request.POST['password']
        form = self.form_class(request.POST)
        user = authenticate(email=email, password=password)

        if user is not None:

            if user.is_active:# and user.is_staff:

                login(request, user)
                return redirect('homepage:index')
        message = "Feil ved innlogging: Brukeren eksisterer ikke"
        return render(request, self.template_name, {'form': form, 'val_error':message},)


def logoutUser(request):

    logout(request)
    return redirect('homepage:index')

class UserSignupFormView(View):

    form_class = UserSignupForm
    template_name = 'homepage/signup.html'

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email') #request.POST['email']
            password = form.cleaned_data.get('password1') #request.POST['password']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('homepage:index')
        message = "Feil ved registrering"
        return render(request, self.template_name, {'form': form, 'val_error': message,})

    def get(self, request):

        form = form = self.form_class(None)
        return render(request, self.template_name, {'form': form})




def fetchStartChecklist():

    if CheckList.objects.filter(is_front=True).count() > 0:
        return createAndReturnChecklist(CheckList.objects.get(is_front=True))

    return None



def createAndReturnChecklist(checklistK):

    checklist_1 = ChecklistLocal(checklistK.name, checklistK.pk, checklistK.is_front)

    for questionK in Question.objects.filter(checkList__pk=checklistK.pk).order_by('priority'):

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

    if request.user.is_authenticated:
        email = request.user.email
    else:
        email = request.POST['email_sender']
    is_filled = True

    if ChecklistAnswer.objects.filter(answer_email=email, checklist=CheckList.objects.get(pk=str(checklist_id))).count() > 0:
        return render(request,'homepage/confirmation.html',
                                  {'query_set': ['Du har allerede svart på denne listen'], 'id': 5})

    answer_checklist = ChecklistAnswer(answer_email=email, checklist=CheckList.objects.get(pk=str(checklist_id)))
    answer_checklist.save()

    answers = []

    for question in Question.objects.filter(checkList__pk=checklist_id):


        if question.isOptions:
            answer = request.POST['answer-option-' + checklist_id + '-' + str(question.id)]
        else:
            answer = request.POST['answer-' + checklist_id + '-' + str(question.id)]

        if answer == "":
            is_filled = False

        answers.append([question.question_text, answer])

        db_answer = Answer(answerText=answer, question=question, answerChecklist=answer_checklist)
        db_answer.save()

    if not is_filled:
        ChecklistAnswer.objects.get(answer_email=email).delete()

    message = 'Takk for dine svar!'

    return render(request, 'homepage/confirmation.html', {'query_set':[message], 'id':4, 'answers': answers,})
    #return render(request, 'homepage/confirmation.html', {})


