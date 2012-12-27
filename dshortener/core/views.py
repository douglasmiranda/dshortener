# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    """
        Você pode conferir a explicação da criação desse Mixin em um post meu:
        http://douglasmiranda.com/artigo/login-required-mixin-django-class-based-generic-views-iv/
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)
