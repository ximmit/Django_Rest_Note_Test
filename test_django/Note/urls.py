from django.urls import path
from .views import NoteView
app_name = "note"


urlpatterns = [path('note/', NoteView.as_view()),
    path('note/<int:pk>', NoteView.as_view()), ]