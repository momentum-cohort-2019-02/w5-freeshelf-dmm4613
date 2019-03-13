from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.CategoriesListView.as_view(), name='categories' ),
    path('category/<slug:slug>', views.CategoriesDetailView.as_view(), name='category_detail'),
] 
