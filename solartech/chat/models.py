from django.db import models

# Create your models here.

class SolarTool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class VirtualAdvisor(models.Model):
    tool = models.OneToOneField(SolarTool, on_delete=models.CASCADE)
    ai_algorithm_version = models.CharField(max_length=50)  # Ajout d'un champ pour la version de l'algorithme d'IA
    recommendations = models.TextField()  # Ajout d'un champ pour les recommandations générées
    # Ajoutez d'autres champs pertinents selon les besoins