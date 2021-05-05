from django.contrib import admin

from .models import Author, Theme, Note


admin.site.register(Author)
admin.site.register(Theme)
admin.site.register(Note)