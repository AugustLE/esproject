from django.contrib import admin

from .models import CheckList, Question
from .models import Option
from .models import Answer
from .models import ChecklistAnswer

# Register your models here.
admin.site.register(Answer)


class OptionInline(admin.StackedInline):

    model = Option
    extra = 1

class QuestionAdmin(admin.ModelAdmin):

    inlines = [OptionInline]

class QuestionInline(admin.StackedInline):

    model = Question
    extra = 0


class ChecklistAdmin(admin.ModelAdmin):

    inlines = [QuestionInline]


class AnswerInline(admin.StackedInline):

    model = Answer
    extra = 0
    fields = ['question', 'answerText']

class ChecklistAnswerAdmin(admin.ModelAdmin):

    inlines = [AnswerInline]

admin.site.register(ChecklistAnswer, ChecklistAnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(CheckList, ChecklistAdmin)
