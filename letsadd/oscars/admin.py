from django.contrib import admin

from .models import Nominee, Ballot, Category, Ceremony, Choice


class CeremonyAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class NomineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'ceremony', 'recipient')


class ChoiceInline(admin.TabularInline):
    model = Choice


class BallotAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Ceremony, CeremonyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Nominee, NomineeAdmin)
admin.site.register(Ballot, BallotAdmin)
admin.site.register(Choice)
