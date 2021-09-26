from configparser import MAX_INTERPOLATION_DEPTH
from email.policy import default
from django.db import models
from django.utils.timezone import now


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
