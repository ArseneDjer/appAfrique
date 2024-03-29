# Generated by Django 5.0.3 on 2024-03-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SolarSystem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        help_text="Localisation géographique de l'installation solaire",
                        max_length=255,
                    ),
                ),
                (
                    "daily_energy_consumption",
                    models.FloatField(
                        help_text="Consommation quotidienne d'énergie en kWh"
                    ),
                ),
                (
                    "sunlight_hours",
                    models.FloatField(
                        help_text="Nombre d'heures d'ensoleillement moyen par jour"
                    ),
                ),
                (
                    "panel_efficiency",
                    models.FloatField(
                        help_text="Efficacité des panneaux solaires en pourcentage"
                    ),
                ),
                (
                    "inverter_efficiency",
                    models.FloatField(
                        help_text="Efficacité de l'onduleur en pourcentage"
                    ),
                ),
                (
                    "battery_capacity",
                    models.FloatField(
                        blank=True,
                        help_text="Capacité de stockage d'énergie des batteries en kWh (facultatif)",
                        null=True,
                    ),
                ),
                (
                    "electronic_devices",
                    models.TextField(
                        help_text="Liste des appareils électroniques utilisés"
                    ),
                ),
                (
                    "number_of_bulbs",
                    models.IntegerField(help_text="Nombre d'ampoules utilisées"),
                ),
                (
                    "recommended_battery_capacity",
                    models.FloatField(
                        blank=True,
                        help_text="Capacité recommandée des batteries en kWh",
                        null=True,
                    ),
                ),
                (
                    "recommended_panel_capacity",
                    models.FloatField(
                        blank=True,
                        help_text="Capacité recommandée des panneaux solaires en kW",
                        null=True,
                    ),
                ),
            ],
        ),
    ]
