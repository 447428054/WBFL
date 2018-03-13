from django.conf.urls import url
from django.contrib import admin

import Note.views as bv

urlpatterns = [
    url(r'^$', bv.AllNotes),
    url(r'^note/(?P<note_id>[0-9]+)$', bv.Note_Page, name='Note_Page'),
    url(r'^edit/(?P<note_id>[0-9]+)$', bv.Edit_Page, name='Edit_page'),
    url(r'^edit/action/$', bv.Edit_action, name='Edit_action'),
]
