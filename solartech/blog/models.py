from django.db import models
from django.contrib.auth.models import User
from tinymce_4.fields import TinyMCEModelField


class Article(models.Model):
    title = models.CharField(max_length=255, help_text="Titre de l'article")
    content = TinyMCEModelField(verbose_name="Contenu", help_text="Contenu de l'article au format HTML")
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True, help_text="Image de couverture de l'article")
    date_published = models.DateTimeField(auto_now_add=True, help_text="Date de publication de l'article")

    def __str__(self):
        return self.title


class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Utilisateur qui a posté sur le forum")
    title = models.CharField(max_length=255, help_text="Titre du message sur le forum")
    content = models.TextField(help_text="Contenu du message sur le forum")
    date_posted = models.DateTimeField(auto_now_add=True, help_text="Date de publication du message sur le forum")

    def __str__(self):
        return self.title
