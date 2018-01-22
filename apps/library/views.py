from django.shortcuts import render, get_object_or_404

from .models import Book, Author, Genre



def index(request):
    return render(
        request, 'library/index.html', {'authors': Author.objects.all()})


def genre(request, genre_id):
    context = {
        'genre': get_object_or_404(Genre, pk=genre_id)
    }
    return render(request, 'library/genre.html', context)


def book(request, book_id):
    context = {
        'book': get_object_or_404(Book, pk=book_id),
    }
    return render(request, 'library/book.html', context)


def author(request, author_id):
    author_obj = get_object_or_404(Author, id=author_id)
    book_ids = Book.objects.only('id').filter(author=author_obj.id)
    book_ids = book_ids.values_list('id', flat=True)
    genres = Genre.objects.filter(book__in=book_ids).distinct()
    context = {
        'author': author_obj,
        'genres': genres
    }
    return render(request, 'library/author.html', context)

