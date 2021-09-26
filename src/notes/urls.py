from django.urls import path

from .views import note_list_view, note_finished_view

app_name = 'notes'

urlpatterns = [
    path('', note_list_view, name='list'),
    path('finished/<int:id>', note_finished_view, name='finished-note'),
]
