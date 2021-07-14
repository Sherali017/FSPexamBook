from django.contrib import admin

from book.models import UserModel, BookModel


@admin.register(UserModel)
class UsermodelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'created_at']

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at',  'is_booked', 'booked_by']
    list_filter = ['created_at']
    search_fields = ['author', 'title', 'created_at']


