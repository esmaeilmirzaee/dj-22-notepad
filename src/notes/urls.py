from django.urls import path

from .views import note_list_view

app_name = 'notes'

urlpatterns = [
    path('', note_list_view, name='list')
]
