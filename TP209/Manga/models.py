from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Manga(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    nombre_tomes = models.IntegerField(blank=False)
    synopsis = models.TextField(null = True, blank = True)
    genre=models.ForeignKey("genre", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur}. C'est un {self.genre} avec {self.nombre_tomes} tomes. Synopsis : {self.synopsis}"
        return chaine

    def dico(self):
        return {"titre": self.titre, "auteur": self.auteur,"nombre_tomes": self.nombre_tomes, "synopsis": self.synopsis}

class Genre(models.Model):
    nomgenre = models.CharField(max_length=20)
    pegi = models.CharField(max_length=30)
    aimedPublic = models.CharField(max_length=100)

    def __str__(self):
        return self.nomgenre

    def dico(self):
        return {"nomgenre": self.nomgenre, "pegi": self.pegi, "public": self.aimedPublic}







