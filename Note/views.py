# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
from django.core import serializers

# Create your views here.


def AllNotes(request):
    notes =serializers.serialize("json", models.Note.objects.all())
    Notes = json.dumps(notes , ensure_ascii=False)
    return HttpResponse(Notes)


def Note_Page(request, note_id):
    note = models.Note.objects.get(pk=note_id)
    Note= json.dumps(note, ensure_ascii=False)
    return HttpResponse(Note)


def Edit_Page(request, note_id):
    if str(note_id) == '0':
        return render(request, 'Note/Edit_Page.html')
    note = models.Note.objects.get(pk=note_id)
    Note=json.dumps(note, ensure_ascii=False)
    return HttpResponse(Note)


def Edit_action(request):
    if request.method =='Get':
        title = request.POST.get('title', 'TITLE')
        content = request.POST.get('content', 'CONTENT')
        note_id= request.POST.get('note_id', '0')

        if note_id == '0':
            models.Note.objects.create(title=title, content=content)
            notes = models.Note.objects.all()
            Notes=json.dumps(notes, ensure_ascii=False)
            return HttpResponse(Notes)

        note=models.Note.objects.get(pk=note_id)
        note.title = title
        note.content = content
        note.save()
        Note=json.dumps(note, ensure_ascii=False)
        return HttpResponse(Note)