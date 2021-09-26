from django.urls import path

from .views import note_list_view, finished_note_view, delete_note_view, recover_note_view

app_name = 'notes'

urlpatterns = [
    path('', note_list_view, name='list'),
    path('finished/<int:id>', finished_note_view, name='finished-note'),
    path('delete/<int:id>', delete_note_view, name='delete-note'),
    path('recover/<int:id>', recover_note_view, name='recover-note')
]
