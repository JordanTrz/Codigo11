from django.urls import path

from . import views

urlpatterns = [
  path('',views.IndexView.as_view(),name='index'),
  path('model',views.ModelView.as_view(),name='model'),
  path('make',views.MakeView.as_view(),name='make'),
  path('model/<int:make_id>',views.MakeModelView.as_view(),name='makemodel'),
  path('category',views.CategoryView.as_view(),name='category'),
  path('fuel',views.FuelView.as_view(),name='fuel'),
  path('transmission',views.TransmissionView.as_view(),name='transmission'),
  path('region',views.RegionView.as_view(),name='region'),
  path('salepost',views.SalePostView.as_view(),name='sale'),
  path('extentuser',views.ExtentUserView.as_view(),name='extentuser'),
  path('user/create',views.UserCreateView.as_view(),name='create_user'),
  path('user/detail/<int:user_id>',views.UserDetailView.as_view(),name='get_user')
]