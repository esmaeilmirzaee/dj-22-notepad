from django.shortcuts import render, get_object_or_404, redirect

from .models import Note


def note_list_view(request):
    undone_notes = Note.objects.filter(finished=False)
    done_notes = Note.objects.filter(finished=True)

    context = {
        'undone_notes': undone_notes,
        'done_notes': done_notes,
    }

    return render(request, 'note_list.html', context)


def finished_note_view(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('notes:list')


def recover_note_view(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect('notes:list')


def delete_note_view(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('notes:list')
