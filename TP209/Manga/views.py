from django.shortcuts import render
from . forms import MangaForm
from . import models
from django.http import HttpResponseRedirect
# Create your views here.


def ajout(request, id):
    form = MangaForm()
    return render(request, "Manga/ajout.html", {"form":form, "id":id})

def traitement(request,id):
    genre = models.Genre.objects.get(pk=id)
    mform = MangaForm(request.POST)
    if mform.is_valid():
        manga=mform.save(commit=False)
        manga.genre = genre
        manga.genre_id = id
        manga.save()
        return HttpResponseRedirect("/Manga/index/")
    else:
        return render(request, 'Manga/index/ajout.html', {'form':mform})

def index(request):
    mList = list(models.Manga.objects.all())
    return render(request, "Manga/index.html", {"Liste": mList})

def affiche(request, id):
    manga=models.Manga.objects.get(pk=id)
    return render(request, "Manga/affiche.html", {"Manga":manga})

def update(request, id):
    manga=models.Manga.objects.get(pk=id)
    mform = MangaForm(manga.dico())
    return render(request, 'Manga/update.html', {"form":mform, "id":id})

def delete(request, id):
    manga = models.Manga.objects.get(pk=id)
    manga.delete()
    return HttpResponseRedirect("/Manga/index")

def traitementupdate(request, id):
    mform=MangaForm(request.POST)
    if mform.is_valid():
        manga = mform.save(commit=False)
        manga.id=id;
        manga.save()
        return HttpResponseRedirect('/Manga/index/')
    else:
        return render(request, "Manga/update.html", {"form":mform, "id":id})

