from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Book

@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(ListView, LoginRequiredMixin):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all().values_list('title', flat=True)
    


class BookDetailView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DetailView
                     ):
    
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'

    

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'books_searched'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        qurey = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=qurey) | Q(author__icontains=qurey)
        )
