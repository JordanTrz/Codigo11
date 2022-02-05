from django.urls import path

from . import views

urlpatterns = [
  path('',views.IndexView.as_view(),name='index'),
  path('model',views.ModelView.as_view(),name='model'),
  path('brand',views.BrandView.as_view(),name='brand'),
  path('brand/<int:brand_id>',views.BrandModelView.as_view(),name='brandmodel'),
  path('category',views.CategoryView.as_view(),name='category'),
  path('fuel',views.FuelView.as_view(),name='brand'),
  path('transmission',views.TransmissionView.as_view(),name='transmission'),
  path('car',views.CarView.as_view(),name='car'),
  path('region',views.RegionView.as_view(),name='region'),
  path('sale',views.SaleView.as_view(),name='sale'),
]