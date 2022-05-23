from django.shortcuts import render
from . forms import GenreForm
from . import models
from django.http import HttpResponseRedirect



def accueil(request):
    gList = list(models.Genre.objects.all())
    return render(request, "Manga/accueil.html", {"Liste": gList})

def ajout(request):
    if request.method == "POST":
        form = GenreForm(request)
        if form.is_valid():
            genre = form.save()
            return render(request,"Manga/affichegenre.html",{"Genre" : genre})
        else:
            return render(request,"Manga/ajoutgenre.html",{"form": form})
    else:
        form = GenreForm()
        return render(request,"Manga/ajoutgenre.html",{"form" : form})

def traitement(request):
    gform = GenreForm(request.POST)
    if gform.is_valid():
        genre=gform.save()
        return HttpResponseRedirect("/Manga/")
    else:
        return render(request, 'Manga/index/ajoutgenre.html', {'form':gform})

def delete(request, id):
    genre = models.Genre.objects.get(pk=id)
    genre.delete()
    return HttpResponseRedirect("/Manga/")

def traitementupdate(request, id):
    gform=GenreForm(request.POST)
    if gform.is_valid():
        genre = gform.save(commit=False)
        genre.id=id;
        genre.save()
        return HttpResponseRedirect('/Manga/')
    else:
        return render(request, "Manga/updategenre.html", {"form":gform, "id":id})

def update(request, id):
    genre=models.Genre.objects.get(pk=id)
    gform = GenreForm(genre.dico())
    return render(request, 'Manga/updategenre.html', {"form":gform, "id":id})


def affiche(request, id):
    genre=models.Genre.objects.get(pk=id)
    liste = models.Manga.objects.filter(genre_id = id)
    return render(request, "Manga/affichegenre.html", {"Genre":genre, "liste":liste})