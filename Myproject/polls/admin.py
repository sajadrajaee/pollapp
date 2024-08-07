from django.contrib import admin
from .models import Choice, Question
# Register your models here.

admin.site.site_title = "This is the site_title"
admin.site.site_header = "This is the site_header"
admin.site.index_title = "This is the index_title"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    #None : it means there is no title for this field or section
    fieldsets = [(None, {'fields':['question_text']}), ('Data Information', {
        'fields':['pub_date'], 'classes':['collapse']}) ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)