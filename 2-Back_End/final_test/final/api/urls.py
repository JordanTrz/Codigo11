from django.urls import path

from . import views

app_name='app'

urlpatterns = [
  path('',views.indexView.as_view(),name='index'),
  path('favorito',views.favoritoView.as_view(),name='favorito'),
  path('favorito/<int:id>',views.favoritoNewView.as_view(),name='favoritonew')
]