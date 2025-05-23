from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class FacturaView(TemplateView):
    template_name = "invoice/invoice.html"
    def get_context_data(self, **kwargs):
        kwargs.setdefault("view", self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs
