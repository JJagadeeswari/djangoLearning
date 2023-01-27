from django.contrib import admin
from .models import Question,Choice


# Register your models here.

"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
"""

#class ChoiceInline(admin.StackedInline):       # --- will use in stack mode;
class ChoiceInline(admin.TabularInline):        # ---- will use in tabular format - less space consuming and more compact to display
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')        # display the respective fields
    list_filter = ['pub_date']                                                    # add filter option in this model
    search_fields = ['question_text']                                             # add search option

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)



