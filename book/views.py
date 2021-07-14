from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from book.models import BookModel, UserModel


class BookListView(ListView):
    template_name = 'content.html'
    queryset = BookModel.objects.all()





