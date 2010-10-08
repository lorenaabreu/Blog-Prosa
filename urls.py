from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    # Example:
    # (r'^blog_prosa/', include('blog_prosa.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    #URL do ADMIN
    (r'^admin/(.*)', admin.site.root),
    #URL da PAG INICIAL
    (r'^$','django.views.generic.date_based.archive_index',
     {'queryset':Artigo.objects.all(),'date_field':'publicacao'}),
    #URL do RSS
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     {'feed_dict': {'ultimos': UltimosArtigos}}),
    #URL dos ARTIGOS
    (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),
    #URL do CONTATOS
    (r'^contato/$','views.contato'),
    #URL de COMENTARIOS
    (r'^comments/',include('django.contrib.comments.urls'))
)

if settings.LOCAL:
    urlpatterns+= patterns('',
    #URL dos ARQ ESTATICO
    (r'^media/(.*)$', 'django.views.static.serve',
     {'document_root':settings.MEDIA_ROOT}),
    )
