from django.contrib import admin
from .models import Question, Choice




# Class to allow adding of choices (By Claude's help)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]



# Register your models here.
admin.site.register(Question, QuestionAdmin)


