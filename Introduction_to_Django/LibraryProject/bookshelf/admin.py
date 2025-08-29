from django.contrib import admin
from .models import Book


# Customize how Book appears in the admin
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar
    list_filter = ('author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')

# Register Book with the custom admin view
admin.site.register(Book, BookAdmin)
