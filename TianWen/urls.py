from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from djangobb_forum import settings as forum_settings
from djangobb_forum.sitemap import SitemapForum, SitemapTopic


sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    # Apps
    url(r'^forum/account/', include('allauth.urls')),
    url(r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
    url(r'^Note/', include('Note.urls', namespace='Note')),
    url(r'^Upload/', include('Upload.urls', namespace='Upload')),
]

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += [
        url(r'^forum/pm/', include('django_messages.urls')),
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)