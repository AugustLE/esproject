from django.contrib import admin

from .models import CheckList
from .models import Question
from .models import Option
from .models import OptionAnswer
from .models import FreeAnswer

# Register your models here.
admin.site.register(CheckList)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(OptionAnswer)
admin.site.register(FreeAnswer)