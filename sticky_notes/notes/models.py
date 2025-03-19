# notes/models.py
from django.db import models


# Create your models here.
class Note(models.Model):
    """Model representing a sticky note.
    Fields:
    - title: CharField for the note title with a maximum length of 255
    characters.
    - content: TextField for the note content.
    - created_at: DateTimeField set to the current date and time when the
    note is created.

    Methods:
    - __str__: Returns a string representation of the note, showing the
    title.

    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Define a ForeignKey for the author's relationship
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ["-created_at"] # Newest notes first

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model representing the author of a sticky note.
    Fields:
    - name: CharField for the author's name.
    
    Methods:
    - __str__: Returns a string representation of the author, showing the
    name.
    
    :param models.Model: Django's base model class.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
