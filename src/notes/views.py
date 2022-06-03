from django.shortcuts import render


from .models import Note


def note_list_view(request):
    list = Note.objects.all()
    context = {
        'object_list': list,
    }

    return render(request, 'note_list.html', context)
