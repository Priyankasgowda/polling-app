
from django.contrib import admin

# Register your models here.
from .models import Question



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

from .models import Choice, Question

admin.site.register(Question, QuestionAdmin)