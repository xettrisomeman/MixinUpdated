from django.views.generic import TemplateView , ListView
from .mixin import OneRequired

from .models import Person



class PageView(OneRequired , TemplateView):
    template_name = 'djangomixin/pageview.htm'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["your_thought"] = kwargs.get('id')
        return context


class PersonListView(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'djangomixin/list.htm'
    
