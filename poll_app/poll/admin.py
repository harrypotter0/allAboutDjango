from django.contrib import admin 

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['qtext']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('qtext', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['qtext']

admin.site.register(Question, QuestionAdmin)

