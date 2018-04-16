# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from Note.SAL import finalGet


# Create your views here.
def toDicts(objects):
    obj_arr = []
    for o in objects:
        obj_arr.append(o.toDict())
    return obj_arr


def AllNotes(request):
    notes =models.Note.objects.all()
    for note in notes:
        (note.Summay, note.Label) = finalGet(note.content, 5)
        note.save()
    notes_dicts=toDicts(notes)
    Notes = json.dumps(notes_dicts , ensure_ascii=False)
    return HttpResponse(Notes,content_type='application/json')


def Note_Page(request, note_id):
    note = models.Note.objects.get(pk=note_id)
    (note.Summay,note.Label)=finalGet(note.content,5)
    note_dict=note.toDict()
    Note= json.dumps(note_dict, ensure_ascii=False)
    return HttpResponse(Note,content_type='application/json')


def Edit_Page(request, note_id):
    if str(note_id) == '0':
        return render(request, 'Note/Edit_Page.html')
    note = models.Note.objects.get(pk=note_id)
    (note.Summay,note.Label)=finalGet(note.content,5)
    note_dict=note.toDict()
    Note=json.dumps(note_dict, ensure_ascii=False)
    return HttpResponse(Note,content_type='application/json')


def Edit_action(request):
    if request.method =='Post':
        title = request.POST.get('title', 'TITLE')
        content = request.POST.get('content', 'CONTENT')
        (Summay,Label)=finalGet(content,5)
        note_id= request.POST.get('note_id', '0')

        if note_id == '0':
            models.Note.objects.create(title=title, content=content,summay=summay,label=label)
            note =models.Note.objects.all()
            note_dicts=toDicts(note)
            Notes=json.dumps(note_dicts, ensure_ascii=False)
            return HttpResponse(Notes,content_type='application/json')

        note=models.Note.objects.get(pk=note_id)
        note.title = title
        note.content = content
        note.Summay=Summay
        note.Label=Label
        note.save()
        note_dict=note.toDict()
        Note=json.dumps(note_dict, ensure_ascii=False)
        return HttpResponse(Note,content_type='application/json')