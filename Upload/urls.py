from django.conf.urls import url
from django.contrib import admin

import Upload.views as bv

urlpatterns = [
    url(r'^$', bv.upload),

]
app_name='Upload',