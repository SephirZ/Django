from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class MangaForm(ModelForm):
    class Meta:
        model = models.Manga
        fields = ('titre', 'auteur', 'nombre_tomes','synopsis')
        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            'nombre_tomes' : _('Nombre de tomes'),
            'synopsis' : _('Synopsis'),
        }

class GenreForm(ModelForm):
    class Meta:
        model = models.Genre
        fields=('nomgenre', 'pegi', 'aimedPublic')
        labels = {
            'nomgenre' : _('Nom du genre'),
            'pegi' : _('Public conseillé (âge)'),
            'aimedPublic' : _('Public visé')
        }