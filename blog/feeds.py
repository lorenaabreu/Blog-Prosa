from django.contrib.syndication.feeds import Feed

from models import Artigo

class UltimosArtigos(Feed):
    title = 'Ultimos Artigos do blog do Prosa'
    link = '/'

    def items(self):
        return Artigo.objects.all()

