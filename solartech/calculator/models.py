# calculator/models.py
from django.db import models

class SolarSystem(models.Model):
    location = models.CharField(
        max_length=255,
        help_text="Localisation géographique de l'installation solaire",
        verbose_name="Localisation"
    )
    daily_energy_consumption = models.FloatField(
        help_text="Consommation quotidienne d'énergie en kWh",
        verbose_name="Consommation quotidienne d'énergie"
    )
    sunlight_hours = models.FloatField(
        help_text="Nombre d'heures d'ensoleillement moyen par jour",
        verbose_name="Heures d'ensoleillement moyen par jour"
    )
    panel_efficiency = models.FloatField(
        help_text="Efficacité des panneaux solaires en pourcentage",
        verbose_name="Efficacité des panneaux solaires"
    )
    inverter_efficiency = models.FloatField(
        help_text="Efficacité de l'onduleur en pourcentage",
        verbose_name="Efficacité de l'onduleur"
    )
    battery_capacity = models.FloatField(
        null=True,
        blank=True,
        help_text="Capacité de stockage d'énergie des batteries en kWh (facultatif)",
        verbose_name="Capacité des batteries (facultatif)"
    )
    electronic_devices = models.TextField(
        help_text="Liste des appareils électroniques utilisés",
        verbose_name="Appareils électroniques utilisés"
    )
    number_of_bulbs = models.IntegerField(
        help_text="Nombre d'ampoules utilisées",
        verbose_name="Nombre d'ampoules utilisées"
    )
    recommended_battery_capacity = models.FloatField(
        null=True,
        blank=True,
        help_text="Capacité recommandée des batteries en kWh",
        verbose_name="Capacité recommandée des batteries"
    )
    recommended_panel_capacity = models.FloatField(
        null=True,
        blank=True,
        help_text="Capacité recommandée des panneaux solaires en kW",
        verbose_name="Capacité recommandée des panneaux solaires"
    )

    def calculate_recommendations(self):
        # Calcul de la puissance solaire requise
        self.required_power = self.daily_energy_consumption / self.sunlight_hours

        # Calcul de la capacité recommandée des batteries (par exemple, deux jours d'autonomie)
        self.recommended_battery_capacity = self.daily_energy_consumption * 2

        # Calcul de la capacité recommandée des panneaux solaires (ajustée en fonction de l'efficacité)
        self.recommended_panel_capacity = (self.required_power / self.panel_efficiency) * 100
