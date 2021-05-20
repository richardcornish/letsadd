from django.urls import path

from .views import chapter_form, ChapterFormView


app_name = 'warhammer'

urlpatterns = [
    path('', chapter_form, name='chapter_form'),
]
