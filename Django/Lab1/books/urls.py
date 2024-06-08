from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('new/', views.book_create, name='book_create'),
    path('<int:index>/', views.book_detail, name='book_detail'),
    path('<int:index>/edit/', views.book_update, name='book_update'),
    path('<int:index>/delete/', views.book_delete, name='book_delete'),
]
