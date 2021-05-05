from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, Author, Theme
from .serializers import NoteSerializer

class NoteView(APIView):
    def get(self, request):
        Notes = Note.objects.all()
        serializer = NoteSerializer(Notes, many=True)
        return Response({"Note": serializer.data})
    def post(self, request):
        Notes = request.data.get('Note')

        serializer = NoteSerializer(data=Notes)
        if serializer.is_valid(raise_exception=True):
            note_saved = serializer.save()
        return Response({"success": "Note '{}' created successfully".format(note_saved.title)})

    def put(self, request, pk):
        saved_note = get_object_or_404(Note.objects.all(), pk=pk)
        data = request.data.get('Note')
        serializer = NoteSerializer(instance=saved_note, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            note_saved = serializer.save()
        return Response({
            "success": "Note '{}' updated successfully".format(note_saved.title)
        })

    def delete(self, request, pk):

        notfordelete = get_object_or_404(Note.objects.all(), pk=pk)
        notfordelete.delete()
        return Response({
            "message": "Note with id `{}` has been deleted.".format(pk)
        }, status=204)