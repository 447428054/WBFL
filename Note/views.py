# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def AllNotes(request):
    notes = models.Note.objects.all()
    return render(request, 'Note/Note.html', {'notes': notes})


def Note_Page(request, note_id):
    note = models.Note.objects.get(pk=note_id)
    return render(request, 'Note/Note_Page.html', {'note': note})


def Edit_Page(request, note_id):
    if str(note_id) == '0':
        return render(request, 'Note/Edit_Page.html')
    note = models.Note.objects.get(pk=note_id)
    return render(request, 'Note/Edit_Page.html', {'note': note})


def Edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    note_id= request.POST.get('note_id', '0')

    if note_id == '0':
        models.Note.objects.create(title=title, content=content)
        notes = models.Note.objects.all()
        return render(request, 'Note/Note.html', {'notes': notes})

    note=models.Note.objects.get(pk=note_id)
    note.title = title
    note.content = content
    note.save()
    return render(request, 'Note/Note_Page.html', {'note': note})