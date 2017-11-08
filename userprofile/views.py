from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from homepage.models import ChecklistAnswer
from homepage.models import Answer
from homepage.CustomClasses.AnswersLocal import AnswersLocal

from .forms import UserChangeForm


class ProfileEditView(View):

    form_class = UserChangeForm
    template_name = 'userprofile/profile.html'

    def get(self, request):

        if not request.user.is_authenticated:

            return redirect('homepage:index')

        email = request.user.email
        company_name = request.user.company_name
        phone = request.user.phone
        first_name = request.user.first_name
        last_name = request.user.last_name
        form = self.form_class(None, initial={'email': email, 'company_name': company_name, 'phone': phone
                                              , 'first_name': first_name, 'last_name': last_name})
        return render(request, self.template_name, {'form': form, 'view_id': 0})

    def post(self, request):

        email = request.POST['email']
        company_name = request.POST['company_name']
        phone = request.POST['phone']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        form = self.form_class(request.POST)
        user = request.user

        if user is not None:

            if user.is_active:# and user.is_staff:

                user.email = email
                user.company_name = company_name
                user.phone = phone
                user.first_name = first_name
                user.last_name = last_name

                if password1 and password2:

                    if password1 == password2:
                        user.set_password(password1)
                        login(request, user)

                    else:
                        message = "FEIL: Passordene matcher ikke"
                        return render(request, self.template_name, {'form': form, 'val_error': message}, )

                user.save()

                return redirect('userprofile:profile')
        message = "Feil"
        return render(request, self.template_name, {'form': form, 'val_error':message},)


class ChecklistView(generic.ListView):

    model = None
    template_name = 'userprofile/user-checklists.html'

    id = 1
    context_object_name = 'answer_objects'

    def get_queryset(self):

        checklists = ChecklistAnswer.objects.filter(answer_email=self.request.user.email)
        answers = []

        for checklist in checklists:
            answers_object = AnswersLocal(checklist.checklist.name, checklist.id)
            for answer in Answer.objects.filter(answerChecklist=checklist):
                answers_object.addAnswer(answer)
            answers.append(answers_object)

        return [answers]

