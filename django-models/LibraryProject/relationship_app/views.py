from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .models import Library

def hello_view(request):
    return HttpResponse

def book_list(request):
    books = Book.objects.all()
    relationship_app/list_books.html
    relationship_app/library_detail.html

    context ={'book_list': books}
    return render(request,'books/book_list.html',context)

from django.views.from django.views.generic import DetailView
from .models import Book
from django.views.generic.detail import DetailView

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_rating'] = book.get_average_rating()

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

UserCreationForm()", "relationship_app/register.html

@user_passes_test", 
"relationship_app/member_view.html", 
"relationship_app/librarian_view.html", "relationship_app/admin_view.html"

from django.contrib.auth.decorators import permission_required 
"relationship_app.can_add_book", "relationship_app.can_change_book"








