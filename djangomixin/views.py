from django.views.generic import TemplateView
from .mixin import OneRequired

class PageView(OneRequired , TemplateView):
    template_name = 'djangomixin/pageview.htm'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["your_thought"] = kwargs.get('id')
        return context
    