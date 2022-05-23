from django.urls import path

from . import views, genre_views

urlpatterns = [
    path('index/', views.index),
    path('index/ajout/<int:id>/', views.ajout),
    path('traitement/<int:id>/', views.traitement),
    path('index/affiche/<int:id>/', views.affiche),
    path('index/update/<int:id>/', views.update),
    path('traitementupdate/<int:id>', views.traitementupdate),
    path('index/delete/<int:id>',views.delete),
    #pages pour les genres

    path('', genre_views.accueil),
    path('ajoutgenre/', genre_views.ajout),
    path('traitementgenre/', genre_views.traitement),
    path('delete/<int:id>', genre_views.delete),
    path('traitementupdategenre/<int:id>', genre_views.traitementupdate),
    path('update/<int:id>/', genre_views.update),
    path('affiche/<int:id>', genre_views.affiche),



]
