# coding:utf-8
from django.views.generic import View, TemplateView
from django.template.response import TemplateResponse
from forms import EncurtarURLForm


class HomeTemplateView1(TemplateView):
    template_name = 'encurtador/home.html'

    def dispatch(self, *args, **kwargs):
        return super(HomeTemplateView, self).dispatch(*args, **kwargs)

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
        form = EncurtarURLForm(request.POST)
        resultado = {}

        if form.is_valid():
            link = form.save()
            resultado['status'] = 'ok'
            resultado['url'] = link.url
            resultado['url_curta'] = link.url_curta
        else:
            resultado['status'] = 'erro'
            resultado['mensagem'] = 'Informe uma url para ser encurtada!'
        contexto['resultado'] = resultado

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