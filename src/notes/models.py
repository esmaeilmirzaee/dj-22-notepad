from django.db import models
from django.utils.timezone import now
from django.shortcuts import reverse

LABEL_CHOICES = (
    ("DA", "dark"),
    ("L", "light"),
    ("D", "danger"),
    ("W", "warning"),
    ("SE", "secondary"),
    ("P", "primary"),
    ("S", "success"),
)


class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField(default=now)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_finished_note_url(self):
        return reverse('notes:finished-note', kwargs={
            'id': self.id
        })

    def get_recover_note_url(self):
        return reverse('notes:recover-note', kwargs={
            'id': self.id
        })

    def get_delete_note_url(self):
        return reverse('notes:delete-note', kwargs={
            'id': self.id
        })

    def get_edit_note_url(self):
        return reverse('notes:edit-note', kwargs={
            'id': self.id,
            'title': self.title,
            'due_date': self.due_date,
        })
