from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Theme(models.Model):
    title = models.CharField(max_length=120)
    Note = models.ForeignKey('Note', related_name='Note', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    #author = models.ForeignKey('Author', related_name='Author', on_delete=models.CASCADE)
    author = models.CharField(max_length=120)

    def __str__(self):
        return self.title