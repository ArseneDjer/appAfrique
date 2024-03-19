# calculator/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import SolarSystem
from .forms import SolarSystemForm

class SolarSystemCreateView(CreateView):
    model = SolarSystem
    form_class = SolarSystemForm
    template_name = 'calculator/calculate.html'
    success_url = reverse_lazy('show_results')

    def form_valid(self, form):
        # Calculs en fonction des appareils électroniques et du nombre d'ampoules
        solar_system = form.save(commit=False)
        solar_system.calculate_recommendations()
        solar_system.save()

        # Ajout des résultats au contexte du template
        context = self.get_context_data(form=form, result=solar_system)
        return self.render_to_response(context)
