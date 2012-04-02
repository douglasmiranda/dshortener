# coding:utf-8
from django.views.generic import View, RedirectView, ListView
from django.template.response import TemplateResponse
from django.views.defaults import page_not_found
from django.http import HttpResponse
import simplejson
import urllib2
from forms import EncurtarURLForm
from models import Link


class HomeTemplateView(View):
    template_name = 'encurtador/home.html'

    def get(self, request, *args, **kwargs):
        contexto = self.get_context_data()
        return TemplateResponse(
            request = self.request,
            template = self.template_name,
            context = contexto,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        contexto = self.get_context_data()
        q = request.POST

        if request.user.is_authenticated():
            q = q.copy()
            q[u'usuario'] = request.user.pk

        form = EncurtarURLForm(q)
        resultado = {}

        if form.is_valid():
            link = form.save()
            resultado['status'] = 'ok'
            resultado['url'] = link.url
            resultado['url_curta'] = link.url_curta
        else:
            resultado['status'] = 'erro'
            resultado['mensagem'] = 'Informe uma URL válida para ser encurtada!'
        contexto['resultado'] = resultado

        if self.request.is_ajax():
            json = simplejson.dumps(resultado)
            return HttpResponse(json, content_type='application/json')

        return TemplateResponse(
            request = self.request,
            template = self.template_name,
            context = contexto,
            **kwargs
        )

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['form_encurtar_url'] = EncurtarURLForm
        return contexto

class GoToRedirectView(RedirectView):
    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid_curto')
        try:
            l = Link.objects.by_uuid(uuid)
            self.url = urllib2.unquote(l.url)
            return super(GoToRedirectView, self).get(request, *args, **kwargs)
        except Link.DoesNotExist:
            return page_not_found(request)

class MyLinksListView(ListView):
    template_name = 'encurtador/my-links.html'
    context_object_name = 'meus_links'
    paginate_by = 20

    def get_queryset(self):
        self.queryset = Link.objects.meus_links(self.request.user)
        return super(MyLinksListView, self).get_queryset()
