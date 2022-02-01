from django.urls import path

from . import views

urlpatterns = [
  path('',views.Index.as_view(),name='index'),
  path('logregs',views.LogRegView.as_view(),name='logregs'),
  path('logreg/<int:usuario_id>',views.LogRegDetailView.as_view())
]