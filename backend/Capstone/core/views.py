from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

# Only authenticated users can view
class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        template_name = "index.html"
        return template_name
