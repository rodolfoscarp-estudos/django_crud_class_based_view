from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', views.UpdateProdutoView.as_view(), name='edit_produto'),
    path('<int:pk>/delete/', views.DeleteProdutoView.as_view(), name='delete_produto')
]
