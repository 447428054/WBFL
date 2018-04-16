# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    Summary=models.TextField(null=True)
    Label=models.TextField(null=True)



    def toDict(self):
        return {'Title':self.title, 'Content':self.content,'Summary':self.Summary,'Label':self.Label}
