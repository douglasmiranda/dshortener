# Create your views here.
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeTemplateView(TemplateView):
    template_name = 'encurtador/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeTemplateView, self).dispatch(*args, **kwargs)