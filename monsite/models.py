from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.email or 'Pas de mail'}"

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=200, blank=True, null=True) #Donne une explication du type d'article   

    def __str__(self):
        return self.titre

class TrainingProgram(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='training_programs/')

    def __str__(self):
        return self.filename