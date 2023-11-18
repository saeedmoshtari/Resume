from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),

]
