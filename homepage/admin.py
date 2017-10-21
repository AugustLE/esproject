from django.contrib import admin

from .models import CheckList
from .models import Question
from .models import Option
from .models import Answer
from .models import ChecklistAnswer

# Register your models here.
admin.site.register(CheckList)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(ChecklistAnswer)