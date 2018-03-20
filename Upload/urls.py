from django.conf.urls import url
from .views import *
import Upload.views as bv
urlpatterns = [
    url(r'^$',bv.registerNormalUser,name='registerNomalUser'),
]