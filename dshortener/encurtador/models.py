from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from util import UUIDCurto


class LinkManager(models.Manager):
    def by_uuid(self, uuid):
        return self.filter(pk=Link.decodificar_uuid(uuid)).get()

    def meus_links(self, usuario):
        return self.filter(usuario=usuario)


class Link(models.Model):
    handler = UUIDCurto()
    url = models.URLField()
    criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    objects = LinkManager()

    @property
    def uuid(self):
        return self.handler.codificar(self.pk)

    @classmethod
    def decodificar_uuid(self, uuid):
        return self.handler.decodificar(uuid)

    @property
    def url_curta(self):
        return settings.ENCURTADOR_SITE_BASE_URL + self.uuid

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ['-criacao']
        get_latest_by = 'criacao'
