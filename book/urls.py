from turtle import home

from django.urls import path

from book.views import BookListView
app_name= 'book'
urlpatterns = [
    path('book/', BookListView.as_view(), name='list')

]