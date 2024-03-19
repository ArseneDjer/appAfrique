from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exemple_variable'] = 'Ceci est une variable d\'exemple'
        return context
