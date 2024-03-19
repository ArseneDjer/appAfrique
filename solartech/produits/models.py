# your_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255, help_text="Nom du produit")
    description = models.TextField(help_text="Description du produit")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Prix du produit")
    quantity_available = models.IntegerField(default=0, help_text="Quantité disponible en stock")
    is_available = models.BooleanField(default=True, help_text="Disponibilité du produit")
    product_image = models.ImageField(upload_to='product_images/', help_text="Image du produit")

    def __str__(self):
        return self.name
    

class EnergyMarketplace(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, help_text="Produit associé sur le marché de l'énergie")
    available_quantity = models.IntegerField(help_text="Quantité disponible sur le marché")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='energy_marketplace_seller', help_text="Vendeur sur le marché de l'énergie")
    # Ajoutez d'autres champs pertinents selon les besoins

class EnergyExchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Utilisateur participant à l'échange d'énergie")
    energy_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantité d'énergie échangée")
    date_shared = models.DateTimeField(auto_now_add=True, help_text="Date et heure de l'échange")
    exchange_type = models.CharField(max_length=50, choices=[('Buy', 'Buy'), ('Sell', 'Sell'), ('Share', 'Share')], help_text="Type d'échange (Achat, Vente, Partage)")
    # Ajoutez d'autres champs pertinents selon les besoins

class Course(models.Model):
    title = models.CharField(max_length=255, help_text="Titre du cours")
    description = models.TextField(help_text="Description du cours")
    video_url = models.URLField(help_text="URL de la vidéo du cours")
    duration_in_minutes = models.IntegerField(help_text="Durée du cours en minutes")
    level = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], help_text="Niveau du cours")
    course_image = models.ImageField(upload_to='course_images/', help_text="Image du cours")

    def __str__(self):
        return self.title


class Sponsorship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals', help_text="Utilisateur qui fait la recommandation")
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrer', help_text="Utilisateur recommandé")
    date_joined = models.DateTimeField(auto_now_add=True, help_text="Date et heure de la recommandation")
