from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='lib_index'),
    path('genre/<int:genre_id>/', views.genre, name='genre'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('author/<int:author_id>/', views.author, name='author'),
]
